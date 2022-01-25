from datetime import date
import json
from pydantic import UUID4


def read_file(file):

    with open(file, "r+", encoding="utf-8") as f:
        databse_registers = json.load(f)
        return databse_registers


def modify_file(registers, file, mode):

    with open(file, mode=mode, encoding="utf8") as f:
        f.seek(0)
        json.dump(registers, f)


def check_user(database_register, operation=None, field_body=None, field_id=None):

    if operation == "create":
        if database_register["email"] != field_body.email:
            return True

    if operation == "login":
        if (
            database_register["email"] == field_body.email
            and database_register["password"] == field_body.password
        ):
            return True

    if field_id:
        if str(database_register["user_id"]) == str(field_id):
            return True


def check_tweet(tweet, tweet_id):

    if tweet["tweet_id"] == str(tweet_id):
        return True


def stringify_user_fields(user, user_id):

    request_dict = user.dict()

    for key in request_dict:
        request_dict[key] = str(request_dict[key])

    request_dict["user_id"] = str(user_id)
    return request_dict


def stringify_tweet_fields(tweet, created_at, updated_at, tweet_id, by=None):

    request_dict = tweet.dict()

    if by:
        request_dict["by"] = by

    request_dict["created_at"] = str(created_at)
    request_dict["updated_at"] = str(updated_at)
    request_dict["tweet_id"] = str(tweet_id)

    return request_dict
