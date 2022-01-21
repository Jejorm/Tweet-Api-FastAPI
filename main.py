from fastapi import FastAPI, status
from models import UserBase, User, UserAuth, Tweet

app = FastAPI()

# Path Operations

@app.get(path="/")
def home():
	return {
		"twitter-api": "Working",
	}


## Users

@app.post(
    path="/signup",
    response_model=UserAuth,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def sign_up():
    pass


@app.post(
    path="/signin",
    response_model=UserAuth,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def sign_in():
    pass


@app.get(
    path="/users",
    response_model=list[User],
    status_code=status.HTTP_200_OK,
    summary="Show all Users",
    tags=["Users"]
)
def show_all_users():
    pass


@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_user():
    pass


@app.put(
    path="/users/{user_id}",
    response_model=UserAuth,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
)
def update_user():
    pass

@app.delete(
    path="/users/{user_id}",
    response_model=UserAuth,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_user():
    pass


## Tweets