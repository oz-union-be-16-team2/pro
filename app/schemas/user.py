from pydantic import BaseModel, Field
from datetime import datetime


# -------------------------
# Request Schemas
# -------------------------

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)


class UserLogin(BaseModel):
    username: str
    password: str


# -------------------------
# Response Schemas
# -------------------------

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserRead(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        from_attributes = True