from fastapi import APIRouter, Depends, HTTPException

from auth.dependencies import get_user
from auth.exceptions import UserException
from auth.models import Token, User, UserLogin, UserRead, UserRegister
from auth.service import AuthService
from common.db.dependencies import get_db

router = APIRouter()

@router.post("/register")
def register(user: UserRegister, db = Depends(get_db)) -> UserRead:
    try:
        created_user: User = AuthService(db).create_user(user)
        return UserRead.model_validate(created_user)
    except UserException as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=str(e)
        )

@router.post("/login")
def login(user: UserLogin, db = Depends(get_db)) -> Token:
    try:
        return AuthService(db).login(user)
    except UserException as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=str(e)
        )

@router.get("/{id}")
def get_user_by_id(id: int, db = Depends(get_db), user = Depends(get_user)) -> UserRead:
    """Finds a user by their ID. Requires authentication as any user."""
    try:
        found_user: User = AuthService(db).get_user_by_id(id)
        return UserRead.model_validate(found_user)
    except UserException as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=str(e)
        )
