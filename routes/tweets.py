import json
from fastapi import Body, status
from models import Tweet
from tools.tools import * 


def Tweets(app):

    database = "data/tweets.json"

   # Post a Tweet
    @app.post(
        path="/tweet",
        response_model=Tweet,
        status_code=status.HTTP_201_CREATED,
        summary="Post a Tweet",
        tags=["Tweets"]
    )
    def tweet(tweet: Tweet = Body(...)):
        """
        This path operation post a tweet in the app

        Parameters:
           - Request Body
               - tweet: Tweet

        Returns a json with the tweet information
           - tweet_id: UUID
           - content: str 
           - created_at: datetime
           - updated_at: datetime | None
           - by: User

       """
        with open(database, "r+", encoding="utf-8") as d:

            databse_registers = json.load(d)

            request_dict = tweet.dict()

            request_dict_serialized = serialize_user(request_dict)

            databse_registers.append(request_dict_serialized)

            d.seek(0)

            json.dump(databse_registers, d)

            return tweet

    # Show all Tweets
    @app.get(
        path="/",
        response_model=list[Tweet],
        status_code=status.HTTP_200_OK,
        summary="Show all Tweets",
        tags=["Tweets"]
    )
    def home():
        """
        This path operation shows all tweets in the app

        Parameters:
           - None

        Returns a json list with all the tweets in the app with the following information:
           - tweet_id: UUID
           - content: str 
           - created_at: datetime
           - updated_at: datetime | None
           - by: User
        """
        with open(database, "r", encoding="utf-8") as d:

            database_registers = json.load(d)

            return database_registers

    # Show a Tweet
    @app.get(
        path="/tweets/{tweet_id}",
        response_model=Tweet,
        status_code=status.HTTP_200_OK,
        summary="Show a Tweet",
        tags=["Tweets"]
    )
    def show_tweet():
        pass

    # Update a tweet
    @app.put(
        path="/tweets/{tweet_id}",
        response_model=Tweet,
        status_code=status.HTTP_200_OK,
        summary="Update a Tweet",
        tags=["Tweets"]
    )
    def update_tweet():
        pass

    # Delete a tweet
    @app.delete(
        path="/tweets/{tweet_id}",
        response_model=Tweet,
        status_code=status.HTTP_200_OK,
        summary="Delete a Tweet",
        tags=["Tweets"]
    )
    def delete_tweet():
        pass
