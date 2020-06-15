#---------------------------------------------------
# Twitbot is still in progress
#---------------------------------------------------
#   To see this in action visit: 
#       https://twitter.com/FulltonThe  
#   (I only ever post using this bot for testing)
#---------------------------------------------------
#   Currently it can:
#       - Update Status (text only)
#       - Search for posts given search terms
#               -Like and Retweet these posts
#---------------------------------------------------
#   Currently working on adding:
#       - Allowing user to imput Status/search terms
#       - Posting images
#       - Posting at specific times a day
#       - Sending Direct Messages
#       - Commenting
#       - GUI interface
#

import os            # Imports os as an environment so that the keys to the API are not shared on the code (for security)    
import tweepy        # Imports Twitter's API
import time          # Allows the like/retweets to be timed (Adheres to Twitter's system)

# Setting up the keys to the API
consumer_key = os.environ.get('twitbotConKey')
consumer_secret = os.environ.get('twitbotConSec')
access_token = os.environ.get('twitbotAccTok')
access_token_secret = os.environ.get('twitbotAccSec')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token,access_token_secret)

# Connecting to the API in a way that adheres to
# the rate limit and notifies when this is reached
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Connects to the user account that will be posted
# on (via the API keys)
user = api.me()

# Updates the user's status
def update_tweet():
    api.update_status('Message Here')
    print('Tweet posted')

# Searches for tweets based off search criteria,
# then, if the tweets have not already been liked,
# it will like and retweet them. If not, it will
# print the error in the console.
def like_and_rt():
    search = ("Python", "Programming")
    number_tweets = 5

    for tweet in tweepy.Cursor(api.search, search).items(number_tweets):
        try:
            tweet.favorite()
            tweet.retweet()
            print('Tweet Retweeted')
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# Calls the functions defined above
# update_tweet()
like_and_rt()