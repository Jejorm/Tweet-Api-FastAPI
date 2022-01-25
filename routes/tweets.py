import uuid
from datetime import datetime
from pydantic import UUID4
from fastapi import Body, Path, HTTPException, status
from models import (
    Tweet,
    TweetResponse,
    TweetAllResponse,
    TweetContent,
    TweetDeleteResponse,
)
from tools.tools import (
    read_file,
    modify_file,
    check_tweet,
    stringify_tweet_fields,
)


def Tweets(app):

    database = "data/tweets.json"

    # Post a Tweet
    @app.post(
        path="/tweet",
        response_model=TweetAllResponse,
        status_code=status.HTTP_201_CREATED,
        summary="Post a Tweet",
        tags=["Tweets"],
    )
    def tweet(tweet: Tweet = Body(...)):
        database_tweet_registers = read_file(database)
        database_user_registers = read_file("data/users.json")

        for user in database_user_registers:
            if user["email"] == tweet.by.email:
                now = datetime.now().strftime("%d/%m/%Y %H:%M")
                tweet_dict_serialized = stringify_tweet_fields(
                    tweet, now, now, uuid.uuid4()
                )
                database_tweet_registers.append(tweet_dict_serialized)
                modify_file(database_tweet_registers, database, "r+")
                return tweet_dict_serialized

        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User email not found")

    # Show all Tweets
    @app.get(
        path="/",
        response_model=list[TweetResponse],
        status_code=status.HTTP_200_OK,
        summary="Show all Tweets",
        tags=["Tweets"],
    )
    def home():

        return read_file(database)

    # Show a Tweet
    @app.get(
        path="/tweets/{tweet_id}",
        response_model=TweetResponse,
        status_code=status.HTTP_200_OK,
        summary="Show a Tweet",
        tags=["Tweets"],
    )
    def show_tweet(tweet_id: UUID4 = Path(...)):

        database_registers = read_file(database)

        for tweet in database_registers:
            if check_tweet(tweet, tweet_id):
                return tweet

        raise (
            HTTPException(status.HTTP_404_NOT_FOUND, detail="Tweet ID does not exists!")
        )

    # Update a tweet
    @app.put(
        path="/tweets/{tweet_id}",
        response_model=TweetResponse,
        status_code=status.HTTP_200_OK,
        summary="Update a Tweet",
        tags=["Tweets"],
    )
    def update_tweet(
        tweet_id: UUID4 = Path(...), tweet_update: TweetContent = Body(...)
    ):

        database_registers = read_file(database)

        for i, tweet in enumerate(database_registers):
            if check_tweet(tweet, tweet_id):
                now = datetime.now().strftime("%d/%m/%Y %H:%M")
                tweet_dict_serialized = stringify_tweet_fields(
                    tweet_update,
                    database_registers[i]["created_at"],
                    now,
                    tweet_id,
                    by=tweet["by"],
                )
                database_registers[i] = tweet_dict_serialized
                modify_file(database_registers, database, "w")

                return database_registers[i]

        raise (
            HTTPException(status.HTTP_404_NOT_FOUND, detail="Tweet ID does not exists!")
        )

    # Delete a tweet
    @app.delete(
        path="/tweets/{tweet_id}",
        response_model=TweetDeleteResponse,
        status_code=status.HTTP_200_OK,
        summary="Delete a Tweet",
        tags=["Tweets"],
    )
    def delete_tweet(tweet_id: UUID4 = Path(...)):

        database_registers = read_file(database)

        for tweet in database_registers:
            if check_tweet(tweet, tweet_id):
                database_registers.remove(tweet)
                modify_file(database_registers, database, "w")
                return TweetDeleteResponse(
                    tweet_id=str(tweet_id), message="Tweet deleted successfully!"
                )

        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail="Tweet ID does not exists!"
        )
