import json
from models import User, UserLogin, UserRegister
from fastapi import Body, status


def Users(app):

    # Register a User
    @app.post(
        path="/signup",
        response_model=User,
        status_code=status.HTTP_201_CREATED,
        summary="Register a User",
        tags=["Users"]
    )
    def sign_up(user: UserRegister = Body(...)):
        """
        This path operation register a user in the app

        Parameters:
           - Request Body
               - user: UserRegister
        
        Returns a json list with the basic user information
           - user_id: UUID
           - email: EmailStr
           - first_name: str
           - last_name: str
           - birthday: date

       """
        with open("data/users.json", "r+", encoding="utf-8") as f:
            results = json.load(f)

            user_dict = dict(user)
            user_dict["user_id"] = str(user_dict["user_id"])
            user_dict["birthday"] = str(user_dict["birthday"])

            results.append(user_dict)

            f.seek(0)
            json.dump(results, f)

        return user

    # Login a User
    @app.post(
        path="/signin",
        response_model=User,
        status_code=status.HTTP_200_OK,
        summary="Login a User",
        tags=["Users"]
    )
    def sign_in():
        pass

    # Show all Users
    @app.get(
        path="/users",
        response_model=list[User],
        status_code=status.HTTP_200_OK,
        summary="Show all Users",
        tags=["Users"]
    )
    def show_all_users():
        """
        This path operation shows all users in the app

        Parameters:
           - None

        Returns a json list with all users in the app
           - user_id: UUID
           - email: EmailStr
           - first_name: str
           - last_name: str
           - birthday: date
        """
        with open("data/users.json", "r", encoding="utf-8") as f:
            results = json.load(f)

            return results

    # Show a User
    @app.get(
        path="/users/{user_id}",
        response_model=User,
        status_code=status.HTTP_200_OK,
        summary="Show a User",
        tags=["Users"]
    )
    def show_user():
        pass

    # Update a User
    @app.put(
        path="/users/{user_id}",
        response_model=User,
        status_code=status.HTTP_200_OK,
        summary="Update a User",
        tags=["Users"]
    )
    def update_user():
        pass

    # Delete a User
    @app.delete(
        path="/users/{user_id}",
        response_model=User,
        status_code=status.HTTP_200_OK,
        summary="Delete a User",
        tags=["Users"]
    )
    def delete_user():
        pass
