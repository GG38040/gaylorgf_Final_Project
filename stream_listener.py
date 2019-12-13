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
    creates extended class object from tweepy.StreamListener class
    """

    # establish auth static variables
    auth = tweepy.OAuthHandler(auth_info.API_KEY, auth_info.API_SECRET_KEY)
    auth.set_access_token(auth_info.ACCESS_TOKEN,
                          auth_info.ACCESS_TOKEN_SECRET)

    # iniate auth variables to tweepy api
    api = tweepy.API(auth)

    def __init__(self, query):
        """
        constructs private data variable for stream query paramater
        """
        self.__query = query

    def on_status(self, status):
        """
        specific stream method from tweepy.org documentation for 
        printing stream data.  Does not utilize __str__ method.  
        """

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
        user_input = input("View more tweets presss 'enter' OR 'q' to quit:")
        if user_input == "q":
            # tweepy.org docs returning false ends twitter stream session
            return False
        else:
            return True

    def on_error(self, status_code):
        """
        checks for status code 420(rate limiter), if recieved ends stream
        """
        if status_code == 420:
            # returning false in on_error disconnents the stream
            return False

    def stream(self, listener):
        """
        accepts listener object to tweepy.Stream() initiates filter()
        """
        my_stream = tweepy.Stream(
            auth=self.api.auth, listener=listener)
        my_stream.filter(track=[self.__query])


# class is custom to Tweepy Module unable to unit test

