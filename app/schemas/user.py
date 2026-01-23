from __future__ import annotations

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class UserRead(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ✅ 추가: 로그인 요청 바디 (Swagger에서 username/password만 보이게)
class LoginRequest(BaseModel):
    username: str
    password: str
