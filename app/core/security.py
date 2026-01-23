from datetime import datetime, timedelta
from typing import Optional

from jose import jwt, JWTError
from app.core.config import settings  # ✅ 추가
from passlib.context import CryptContext

# ⚠️ 실서비스면 반드시 .env로 빼야 함
SECRET_KEY = "dev-secret-key-change-me"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# bcrypt 오류 방지용 설정
pwd_context = CryptContext(
    schemes=["pbkdf2_sha256", "bcrypt"],
    deprecated="auto",
)


# ======================
# Password
# ======================
def hash_password(password: str) -> str:
    """
    비밀번호 해싱
    """
    # bcrypt는 72byte 제한 → 안전하게 슬라이싱
    return pwd_context.hash(password[:72])


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# ======================
# JWT
# ======================
def create_access_token(subject: str):
    to_encode = {"sub": subject}
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict:
    """
    JWT 디코딩 (get_current_user에서 사용)
    """
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except JWTError:
        raise

