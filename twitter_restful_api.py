"""
Greg Gaylor
Class: CS 521-Fall 2
Date: 12/8/2019
Final Project 
Description: Twitter API
"""

import tweepy
import auth_info


class Twit_restful():
    """
    """
    # static variables for api
    auth = tweepy.OAuthHandler(auth_info.API_KEY, auth_info.API_SECRET_KEY)
    auth.set_access_token(auth_info.ACCESS_TOKEN,
                          auth_info.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    def __init__(self):
        """
        """
        self.search_user = None
        self.search = None

    def __str__(self):
        """
        """
        return('{}'.format(self.get_public_tweets(),
                           '{}'.format(self.get_user(),
                                       '{}'.format(self.search_twitter()))))

    def get_public_tweets(self):
        """
        """
        # prints tweets from public timeline
        tweet_text_list = []
        public_tweets = self.api.home_timeline()

        # print last 10 tweets from timeline
        for i in range(1, 11):
            tweet_text_list.append(public_tweets[i].text)

        s = "\n"
        return s.join(tweet_text_list)

    def get_user(self, search_user):
        """
        """
        # gets a user prints their screen name and follower count
        user = self.api.get_user(search_user)
        user_search_tuple = ('Follower Count =', str(user.followers_count),
                             str(user.name), 'is account verified =', str(user.verified))
        return ' '.join(user_search_tuple)

    def search_twitter(self, search):
        """
        """
        # search 10 items api.search q="[search]"
        search_results_list = []
        search_tweepy = tweepy.Cursor(self.api.search, q=search).items(3)
        for item in search_tweepy:
            search_results_list.append(item.text)

        s = "\n"
        return s.join(search_results_list)


if __name__ == '__main__':

    twitter_stuff = Twit_restful()
    print(twitter_stuff.get_user('gaylorIii'))
    # print(twitter_stuff.search_twitter('#python'))
    # print(twitter_stuff.get_public_tweets())
