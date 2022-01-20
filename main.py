from fastapi import FastAPI
from models import UserBase, User, UserLogin, Tweet

app = FastAPI()

@app.get(path="/")
def home():
	return {
		"twitter-api": "Working",
	}