from models import User, UserLogin, UserRegister
from fastapi import status


def Users(app):

	### Register a User
	@app.post(
			path="/signup",
			response_model=User,
			status_code=status.HTTP_201_CREATED,
			summary="Register a User",
			tags=["Users"]
	)
	def sign_up():
         """
        Signup

        This path operation register a user in the app.

        Params:
            - Request Body
                - user: UserRegister
        
        Returns a json with the basic user information
            - user_id: UUID
            - email: EmailStr
            - first_name: str
            - last_name: str
            - birthday: str
        """
        pass



	### Login a User
	@app.post(
			path="/signin",
			response_model=User,
			status_code=status.HTTP_200_OK,
			summary="Login a User",
			tags=["Users"]
	)
	def sign_in():
			pass

	### Show all Users
	@app.get(
			path="/users",
			response_model=list[User],
			status_code=status.HTTP_200_OK,
			summary="Show all Users",
			tags=["Users"]
	)
	def show_all_users():
			pass

	### Show a User
	@app.get(
			path="/users/{user_id}",
			response_model=User,
			status_code=status.HTTP_200_OK,
			summary="Show a User",
			tags=["Users"]
	)
	def show_user():
			pass

	### Update a User
	@app.put(
			path="/users/{user_id}",
			response_model=User,
			status_code=status.HTTP_200_OK,
			summary="Update a User",
			tags=["Users"]
	)
	def update_user():
			pass

	### Delete a User
	@app.delete(
			path="/users/{user_id}",
			response_model=User,
			status_code=status.HTTP_200_OK,
			summary="Delete a User",
			tags=["Users"]
	)
	def delete_user():
			pass
