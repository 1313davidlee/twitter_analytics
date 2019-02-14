import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
        def __init__(self):

            #twitter api keys and tokens from dev console
            consumer_key = 'mz8pWcnrrkwj6CBkpAPbRmXoq'
            consumer_secret = 'mz8pWcnrrkwj6CBkpAPbRmXoq'
            access_token = '1088659657672085504-s3cWorCMJXV9o93gcZHbd9hEuT5May'
            access_secret = 'TXrQsrMaozaNJEyRmprjjggVFYxsvlkWtRZib620k5BOV'

            #attempt authentication

            try:
                #create OAuthHandler object
                self.auth = OAuthHandler(consumer_key, consumer_secret)
                #set access token and access_secret
                self.auth.set_access_token(access_token, access_secret)
                #create tweepy API object to fetch tweets from Twitter
                self.api = tweepy.API(self.auth)
            except:
                print("Error: authentication failed")

        def clean_tweet(self, tweet):
            #function to strip links and special characters using regex statement
            return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])
                                    |(\w+:\/\/\S+)", " ", tweet).split())

        def get_tweet_sentiment(self, tweet):
            #function to classify sentiment of passed tweet using textblob's sentiment method
            analysis = TextBlob(self.clean_tweet(tweet))

            if analysis.sentiment.polarity > 0:
                    return 'positive'
            elif analysis.sentiment.polarity == 0:
                    return 'neutral'
            else:
                    return 'negative'

        def get_tweets(self, query, count = 10):
                #main function to fetch tweets and parse them

                #empty list to store tweets
                tweets = []

                try:
                        fetched_tweets = self.api.search(q = query, count = count)

                        #parse tweets one at a time
                        for tweet in fetched_tweets:
                                #dictionary to store quired params of a tweets
                                parsed_tweet = {}

                                #saving text of tweet
                                parsed_tweet['text'] = tweet.text
                                #saving sentiment of tweets
                                parsed_tweet
