from datetime import date
import json
from pydantic import UUID4


def read_file(file):

    with open(file, "r+", encoding="utf-8") as f:

        databse_registers = json.load(f)

        return databse_registers


def write_file(registers, file):

    with open(file, "r+", encoding="utf-8") as f:

        f.seek(0)

        json.dump(registers, f)


def check_user(database_register, operation, field_body=None, field_id=None):

    if operation == "register":
        if database_register["email"] != field_body.email:
            return True 

    if operation == "login":
        if database_register["email"] == field_body.email and database_register["password"] == field_body.password:
            return True
    
    if operation == "user_id":
        if str(database_register["user_id"]) == str(field_id):
            return True


def serialize_user(user, user_id=None):

    if type(user) is not dict:
        request_dict = user.dict()
    else:
        request_dict = user

    serialize_formats = [UUID4, date]

    for key in request_dict:
        value = request_dict[key]

        if type(value) is dict:
            serialize_user(value)
            continue

        if type(value) in serialize_formats:
            request_dict[key] = str(value)

    if user_id:
        request_dict[f"user_id"] = str(user_id)


    return request_dict


def overwrite_file(registers, file):

    with open(file, "w", encoding="utf-8") as f:

        f.seek(0)

        json.dump(registers, f)
    