import uuid
from fastapi import Body, Path, HTTPException, status
from models import UserAllResponse, UserLogin, UserUpdate, UserMessages, User
from tools.tools import read_file, modify_file, check_user, stringify_user_fields
from pydantic import UUID4


def Users(app):

    database = "data/users.json"

    # Register a User
    @app.post(
        path="/signup",
        response_model=UserAllResponse,
        status_code=status.HTTP_201_CREATED,
        summary="Register a User",
        tags=["Users"],
    )
    def sign_up(user_register: UserUpdate = Body(...)):
        """
        This path operation register an user in the app

        Parameters:
           - Request Body
               - user: UserUpdate

        Returns a json with the basic user information
           - email: EmailStr
           - first_name: str
           - last_name: str
           - birthday: date | None
           - password: str
           - user_id: UUID4
        """

        databse_registers = read_file(database)

        for user in databse_registers:
            if not check_user(user, operation="create", field_body=user_register):
                raise HTTPException(
                    status.HTTP_400_BAD_REQUEST, detail="Email already registered"
                )

        user_dict_serialized = stringify_user_fields(user_register, uuid.uuid4())
        databse_registers.append(user_dict_serialized)
        modify_file(databse_registers, database, "r+")
        return user_dict_serialized

    # Login a User
    @app.post(
        path="/signin",
        response_model=UserMessages,
        status_code=status.HTTP_200_OK,
        summary="Login a User",
        tags=["Users"],
    )
    def sign_in(user_login: UserLogin = Body(...)):
        """
        This path operation login an user in the app

        Parameters:
           - Request Body
               - user: UserLogin

        Returns a json with the user login information:
           - email: EmailStr
           - message: str
        """

        database_registers = read_file(database)

        for user in database_registers:
            if check_user(user, operation="login", field_body=user_login):
                return UserMessages(message="Login Successfully!", **user)

        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, detail="Email or Password incorrect"
        )

    # Show all Users
    @app.get(
        path="/users",
        response_model=list[User],
        status_code=status.HTTP_200_OK,
        summary="Show all Users",
        tags=["Users"],
    )
    def show_all_users():
        """
        This path operation shows all users in the app

        Parameters:
           - None

        Returns a json list with all users in the app with the following information:
           - email: EmailStr
           - first_name: str
           - last_name: str
           - birthday: date | None
        """

        return read_file(database)

    # Show a User
    @app.get(
        path="/users/{user_id}",
        response_model=User,
        status_code=status.HTTP_200_OK,
        summary="Show a User",
        tags=["Users"],
    )
    def show_user(user_id: UUID4 = Path(...)):
        """
        This path operation shows an user in the app

        Parameters:
           - Path Parameter
               - user_id: UUID4

        Returns a json with user information:
           - email: EmailStr
           - first_name: str
           - last_name: str
           - birthday: date | None
        """

        database_registers = read_file(database)

        for user in database_registers:
            if check_user(user, field_id=user_id):
                return user

        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, detail="User ID does not exists!"
        )

    # Update a User
    @app.put(
        path="/users/{user_id}",
        response_model=UserAllResponse,
        status_code=status.HTTP_200_OK,
        summary="Update a User",
        tags=["Users"],
    )
    def update_user(user_id: UUID4 = Path(...), user_update: UserUpdate = Body(...)):
        """
        This path operation update an user in the app

        Parameters:
           - Path Parameter:
               - user_id: UUID4
           - Response Body:
               - user_update: UserUpdate

        Returns a json with all user information:
           - email: EmailStr
           - first_name: str
           - last_name: str
           - birthday: date | None
           - password: str
           - user_id: UUID4
        """

        database_registers = read_file(database)

        for user in database_registers:
            if not check_user(user, operation="create", field_body=user_update):
                raise HTTPException(
                    status.HTTP_404_NOT_FOUND,
                    detail="User ID does not exists or Email already registered!",
                )

        for i, user in enumerate(database_registers):
            if check_user(user, field_id=user_id):
                user_dict_serialized = stringify_user_fields(user_update, user_id)
                database_registers[i] = user_dict_serialized
                modify_file(database_registers, database, "w")
                return database_registers[i]

        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="User ID does not exists! or Email already registered!",
        )

    # Delete a User
    @app.delete(
        path="/users/{user_id}",
        response_model=UserMessages,
        status_code=status.HTTP_200_OK,
        summary="Delete a User",
        tags=["Users"],
    )
    def delete_user(user_id: UUID4 = Path(...)):
        """
        This path operation delete an user in the app

        Parameters:
           - Path Parameter:
               - user_id: UUID4

        Returns a json with email and a message of success:
           - email: EmailStr
           - message: str
        """

        database_registers = read_file(database)

        for user in database_registers:

            if check_user(user, field_id=user_id):
                database_registers.remove(user)
                modify_file(database_registers, database, "w")
                return UserMessages(message="User deleted successfully!", **user)

        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, detail="User ID does not exist!"
        )
