from fastapi import FastAPI

# Users
from routes.users import Users

# Tweets
from routes.tweets import Tweets

app = FastAPI()
Users(app)
Tweets(app)

@app.get("/")
def inicio():
    return {"Hello": "World"}
