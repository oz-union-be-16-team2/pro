from __future__ import annotations

from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.models.user import User
from app.schemas.user import UserCreate, UserRead, TokenResponse
from app.core.security import verify_password, create_access_token, decode_access_token
from app.services.user_service import create_user


router = APIRouter(prefix="/auth", tags=["Auth"])

# Swagger에서 "Authorize" 버튼 눌렀을 때 들어오는 토큰 소스
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# -------------------------
# Dependency: get_current_user
# -------------------------
async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """
    Authorization: Bearer <token> 에서 토큰을 꺼내서
    검증 -> sub(username)로 User 조회 -> User 반환
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_access_token(token)  # 실패하면 None
    if payload is None:
        raise credentials_exception

    username: Optional[str] = payload.get("sub")
    if not username:
        raise credentials_exception

    user = await User.get_or_none(username=username)
    if not user:
        raise credentials_exception

    # (선택) is_active 필드 있으면 비활성 차단
    if hasattr(user, "is_active") and user.is_active is False:
        raise HTTPException(status_code=403, detail="Inactive user")

    return user


# -------------------------
# Routes
# -------------------------
@router.get("/health")
async def auth_health():
    return {"status": "ok"}


@router.post(
    "/signup",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
async def signup(payload: UserCreate):
    """
    POST /api/v1/auth/signup
    - username 중복 체크
    - 비밀번호 해싱 처리 후 저장
    """
    exists = await User.get_or_none(username=payload.username)
    if exists:
        raise HTTPException(status_code=409, detail="Username already exists")

    user = await create_user(payload)
    return user


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    POST /api/v1/auth/login
    - OAuth2PasswordRequestForm 사용 (Swagger 테스트 쉬움)
    - username/password 검증
    - Access Token 발급
    """
    user = await User.get_or_none(username=form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token(subject=user.username)
    return TokenResponse(access_token=token)


@router.get(
    "/me",
    response_model=UserRead,
    status_code=status.HTTP_200_OK,
)
async def read_me(current_user: User = Depends(get_current_user)):
    """
    GET /api/v1/auth/me
    - 현재 로그인 유저 정보 조회 (보호됨)
    """
    return current_user