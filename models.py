from datetime import date
from pydantic import BaseModel, EmailStr, Field, UUID4


# User
class UserEmail(BaseModel):
    email: EmailStr = Field(...)


class UserId(BaseModel):
    user_id: UUID4 = Field(...)


class UserPassword(BaseModel):
    password: str = Field(..., min_length=8, max_length=64)


class User(UserEmail):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birthday: date | None = Field(default=None)


class Auth(UserId, UserPassword):
    ...


class UserUpdate(UserPassword, User):
    ...


class UserAllResponse(Auth, User):
    ...


class UserLogin(UserPassword, UserEmail):
    ...


class UserMessages(UserEmail, UserId):
    message: str = Field(...)


# Tweet
class TweetContent(BaseModel):
    content: str = Field(...)


class TweetID(BaseModel):
    tweet_id: UUID4 = Field(...)


class Tweet(TweetContent):
    by: UserEmail = Field(...)


class TweetDeleteResponse(TweetID):
    message: str = Field(...)


class TweetResponse(Tweet):
    created_at: str = Field(...)
    updated_at: str = Field(...)


class TweetAllResponse(TweetID, TweetResponse):
    ...
