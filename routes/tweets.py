from models import Tweet
from fastapi import status


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
    def tweet():
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
