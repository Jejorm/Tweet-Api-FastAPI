from datetime import date, datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class User_Email(BaseModel):
    email: EmailStr = Field(...)


class User_Id(BaseModel):
    user_id: UUID = Field(...)


class UserPassword(BaseModel):
    password: str = Field(..., min_length=8, max_length=64)


class User(User_Email):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birthday: date | None = Field(default=None)


class Auth(User_Id, UserPassword):
    ...


class UserShow(User):
    ...

class UserUpdate(UserPassword, User):
    ...


class UserAllResponse(Auth, User):
    ...


class UserLogin(UserPassword, User_Email):
    ...


class UserMessages(User_Email):
    message: str = Field(...)





class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(..., min_length=1, max_length=256)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime | None = Field(default=None)
    by: User = Field(...)
