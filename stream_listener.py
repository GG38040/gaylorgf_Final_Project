"""
Greg Gaylor
Class: CS 521-Fall 2
Date: 12/8/2019
Final Project 
Description: Twitter API
"""

import tweepy
import auth_info


class Stream_listener(tweepy.StreamListener):
    """
    """

    # establish auth static variables
    auth = tweepy.OAuthHandler(auth_info.API_KEY, auth_info.API_SECRET_KEY)
    auth.set_access_token(auth_info.ACCESS_TOKEN,
                          auth_info.ACCESS_TOKEN_SECRET)

    # iniate auth variables to tweepy api
    api = tweepy.API(auth)

    def __init__(self, query):
        self.__query = query

    def on_status(self, status):

        
        if hasattr(status, 'retweeted_status'):
            try:
                print(status.retweeted_status.extend_tweet['full_text'])
            except AttributeError:
                print(status.retweeted_status.text)
        else:
            try:
                print(status.extended_tweet['full_text'])
            except AttributeError:
                print(status.text)
        user_input = input("View more tweets from stream? 'q' quit:")
        if user_input == "q":
            return False
        else:
            return True
            

    def on_error(self, status_code):
        if status_code == 420:
            # returning false in on_error disconnents the stream
            return False

    def stream(self, listener):
        """
        """
        my_stream = tweepy.Stream(
            auth=self.api.auth, listener=listener)
        my_stream.filter(track=[self.__query])

