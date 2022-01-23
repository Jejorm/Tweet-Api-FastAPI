from datetime import date, datetime
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


def check_user(user_database, operation, user_body=None, user_id=None):

    if operation == "email":
        if user_database["email"] != user_body.email:
            return True 

    if operation == "login":
        if user_database["email"] == user_body.email and user_database["password"] == user_body.password:
            return True
    
    if operation == "user_id":
        if str(user_database["user_id"]) == str(user_id):
            return True


def serialize_user(user, user_id=None):

    request_dict = user.dict()

    serialize_formats = [UUID4, date, datetime]

    for key in request_dict:
        value = request_dict[key]

        if type(value) is dict:
            serialize_user(value)
            continue

        if type(value) in serialize_formats:
            request_dict[key] = str(value)

    if user_id:
        request_dict["user_id"] = str(user_id)

    return request_dict


def overwrite_file(registers, file):

    with open(file, "w", encoding="utf-8") as f:

        f.seek(0)

        json.dump(registers, f)
    