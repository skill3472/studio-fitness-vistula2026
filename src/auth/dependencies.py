from fastapi import Depends, Security
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from auth.models import User
from auth.service import AuthService
from common.db.dependencies import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")


def get_user(
    token: str = Security(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    return AuthService(db).get_current_user(token)
