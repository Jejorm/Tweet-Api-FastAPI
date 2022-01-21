import json
import pprint
from fastapi import Body, status
from models import Tweet


def Tweets(app):

    # Show all Tweets
    @app.get(
        path="/tweets",
        response_model=list[Tweet],
        status_code=status.HTTP_200_OK,
        summary="Show all Tweets",
        tags=["Tweets"]
    )
    def show_all_tweets():
        pass

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
        with open("data/tweets.json", "r+", encoding="utf-8") as f:

            results = json.load(f)

            tweet_dict = tweet.dict()

            tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
            tweet_dict["created_at"] = str(tweet_dict["created_at"])
            tweet_dict["updated_at"] = str(tweet_dict["updated_at"])

            tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
            tweet_dict["by"]["birthday"] = str(tweet_dict["by"]["birthday"])

            results.append(tweet_dict)

            f.seek(0)
            json.dump(results, f)

            return tweet


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
