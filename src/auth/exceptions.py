from fastapi import status


class UserException(BaseException):
    """Base user exception."""

    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR


class UserAlreadyExists(UserException):
    """User with this username already exists in the database."""

    status_code: int = status.HTTP_409_CONFLICT


class InvalidCredentials(UserException):
    """Username/password pair provided during login was incorrect."""

    status_code: int = status.HTTP_401_UNAUTHORIZED


class InvalidTokenError(UserException):
    """JWT token is invalid or not present."""

    status_code: int = status.HTTP_401_UNAUTHORIZED


class UserNotFoundError(UserException):
    """User with provided ID not found."""

    status_code: int = status.HTTP_404_NOT_FOUND
