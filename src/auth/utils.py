from datetime import UTC, datetime, timedelta

import bcrypt
import jwt

from auth.exceptions import InvalidTokenError
from config import settings


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password.encode())


def create_access_token(user_id: int) -> str:
    expire = datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": str(user_id), "exp": expire}
    return jwt.encode(
        payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )


def resolve_user_id_from_token(token: str) -> int:
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        return int(payload["sub"])
    except (jwt.InvalidTokenError, KeyError, ValueError) as e:
        raise InvalidTokenError("The provided JWT auth token is invalid.") from e
