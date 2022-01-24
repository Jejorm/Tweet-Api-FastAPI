import uuid
from datetime import datetime
from pydantic import UUID4
from fastapi import Body, Path, HTTPException, status
from models import TweetPost, TweetResponse, TweetAllResponse, TweetUpdate, TweetDeleteResponse
from tools.tools import read_file, write_file, overwrite_file


def Tweets(app):

    database = "data/tweets.json"

   # Post a Tweet
    @app.post(
        path="/tweet",
        response_model=TweetAllResponse,
        status_code=status.HTTP_201_CREATED,
        summary="Post a Tweet",
        tags=["Tweets"]
    )
    def tweet(tweet: TweetPost = Body(...)):

        database_registers = read_file(database)

        tweet_dict_serialized = tweet.dict()
        tweet_dict_serialized["tweet_id"] = str(uuid.uuid4())
        tweet_dict_serialized["created_at"] = str(datetime.now().strftime("%d/%m/%Y %H:%M"))
        tweet_dict_serialized["updated_at"] = str(datetime.now().strftime("%d/%m/%Y %H:%M"))

        database_registers.append(tweet_dict_serialized)

        write_file(database_registers, database)

        return tweet_dict_serialized


    # Show all Tweets
    @app.get(
        path="/",
        response_model=list[TweetResponse],
        status_code=status.HTTP_200_OK,
        summary="Show all Tweets",
        tags=["Tweets"]
    )
    def home():

        return(read_file(database))

    # Show a Tweet
    @app.get(
        path="/tweets/{tweet_id}",
        response_model=TweetResponse,
        status_code=status.HTTP_200_OK,
        summary="Show a Tweet",
        tags=["Tweets"]
    )
    def show_tweet(tweet_id: UUID4 = Path(...)):
        
        database_registers = read_file(database)

        for tweet in database_registers:
            
            if tweet["tweet_id"] == str(tweet_id):
                return tweet

        raise(HTTPException(status.HTTP_404_NOT_FOUND, detail="Tweet ID does not exists!"))

    # Update a tweet
    @app.put(
        path="/tweets/{tweet_id}",
        response_model=TweetResponse,
        status_code=status.HTTP_200_OK,
        summary="Update a Tweet",
        tags=["Tweets"]
    )
    def update_tweet(tweet_id: UUID4 = Path(...), tweet_update: TweetUpdate = Body(...)):

        database_registers = read_file(database)

        for i, tweet in enumerate(database_registers):

            if tweet["tweet_id"] == str(tweet_id):

                tweet_dict_serialized = tweet_update.dict()

                tweet_dict_serialized["by"] = database_registers[i]["by"]
                tweet_dict_serialized["tweet_id"] = str(tweet_id)
                tweet_dict_serialized["created_at"] = database_registers[i]["created_at"]
                tweet_dict_serialized["updated_at"] = str(datetime.now().strftime("%d/%m/%Y %H:%M"))


                database_registers[i] = tweet_dict_serialized

                overwrite_file(database_registers, database)

                return database_registers[i]

        raise(HTTPException(status.HTTP_404_NOT_FOUND, detail="Tweet ID does not exists!"))


    # Delete a tweet
    @app.delete(
        path="/tweets/{tweet_id}",
        response_model=TweetDeleteResponse,
        status_code=status.HTTP_200_OK,
        summary="Delete a Tweet",
        tags=["Tweets"]
    )
    def delete_tweet(tweet_id: UUID4 = Path(...)):

        database_registers = read_file(database)

        for tweet in database_registers:
            if tweet["tweet_id"] == str(tweet_id):
                database_registers.remove(tweet)
                overwrite_file(database_registers, database)

                return TweetDeleteResponse(tweet_id=str(tweet_id), message="Tweet deleted successfully!")    
        
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Tweet ID does not exists!")