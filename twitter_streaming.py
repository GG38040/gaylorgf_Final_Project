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

    def on_error(self, status_code):
        if status_code == 420:
            # returning false in on_error disconnents the stream
            return False

    def stream(self):
        """
        """
        my_stream = tweepy.Stream(auth=self.api.auth, listener=stream_listener)
        my_stream.filter(track=[self.__query])


if __name__ == '__main__':

    # intiate stream and enter track query
    stream_listener = Stream_listener('dominos')
    stream_listener.stream()
