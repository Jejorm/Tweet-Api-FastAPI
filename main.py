from datetime import date
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field
from fastapi import FastAPI

app = FastAPI()

# Models

class UserBase(BaseModel):
	user_id: UUID = Field(...)
	email: EmailStr = Field(...)


class UserLogin(UserBase):
	password: str = Field(..., min_length=8)


class User(UserBase):
	first_name: str = Field(..., min_length=1, max_length=50)
	last_name: str = Field(..., min_length=1, max_length=50)
	birthday: date | None =  Field(default=None)


class Tweet(BaseModel):
	pass


@app.get(path="/")
def home():
	return {
		"twitter-api": "Working",
	}