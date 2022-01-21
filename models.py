from datetime import date, datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
	user_id: UUID = Field(...)
	email: EmailStr = Field(...)


class User(UserBase):
	first_name: str = Field(..., min_length=1, max_length=50)
	last_name: str = Field(..., min_length=1, max_length=50)
	birthday: date | None =  Field(default=None)


class UserAuth(UserBase):
	password: str = Field(..., min_length=8, max_length=64)


class Tweet(BaseModel):
	tweet_id: UUID = Field(...)
	content: str = Field(..., min_length=1, max_length=256)
	created_at: datetime = Field(default=datetime.now())
	updated_at: datetime | None = Field(default=None)
	by: User = Field(...)