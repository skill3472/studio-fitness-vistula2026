from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    password_hash: str
    created_at: datetime

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )

class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(UserRegister):
    pass

class UserRead(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    username: str
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"