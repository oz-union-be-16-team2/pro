from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password


async def create_user(user_in: UserCreate) -> User:
    """
    회원가입용 유저 생성
    - password 해싱 후 저장
    """
    hashed_pw = hash_password(user_in.password)

    user = await User.create(
        username=user_in.username,
        password_hash=hashed_pw,
    )
    return user