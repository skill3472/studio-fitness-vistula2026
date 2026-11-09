from sqlalchemy import select
from sqlalchemy.orm import Session

from auth.exceptions import InvalidCredentials, UserAlreadyExists, UserNotFoundError
from auth.models import Token, UserLogin, UserRegister
from auth.models import User as UserSchema
from auth.schema import User
from auth.utils import (
    create_access_token,
    hash_password,
    verify_password,
    resolve_user_id_from_token,
)


class AuthService:
    """Service handling authentication."""

    def __init__(self, db: Session):
        self.db: Session = db

    def create_user(self, schema: UserRegister) -> UserSchema:
        """
        Creates a new user in the database or raises if already exists.

        Args:
            schema (UserRegister): Username and password of user to register

        Returns:
            UserSchema: Schema of created user

        Raises:
            UserAlreadyExists: When user with provided username already exists.
        """
        existing = self.db.execute(
            select(User).where(User.username == schema.username)
        ).scalar_one_or_none()
        if existing:
            raise UserAlreadyExists(
                f"A user with the provided username ({schema.username}) already exists!"
            )

        hashed = hash_password(schema.password)

        user: User = User(
            username=schema.username,
            password_hash=hashed,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return UserSchema.model_validate(user)

    def login(self, schema: UserLogin) -> Token:
        user: User | None = self.db.execute(
            select(User).where(User.username == schema.username)
        ).scalar_one_or_none()
        if user is None or not verify_password(schema.password, user.password_hash):
            raise InvalidCredentials("Incorrect name or password.")

        return Token(access_token=create_access_token(user.id))

    def get_current_user(self, token: str) -> UserSchema:
        user_id: int = resolve_user_id_from_token(token)

        user: User | None = self.db.get(User, user_id)
        if user is None:
            raise InvalidCredentials("Could not validate credentials.")

        return UserSchema.model_validate(user)

    def get_user_by_id(self, id: int) -> UserSchema:
        user: User | None = self.db.get(User, id)
        if user is None:
            raise UserNotFoundError("User with provided ID was not found.")

        return UserSchema.model_validate(user)
