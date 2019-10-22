import tweepy
from termcolor import colored
from config import create_api, get_keyword
import logging


# Create API object
api = create_api()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# get keyword
keyword = get_keyword()
logger.info('Tracking tweets with keyword: {}'.format(keyword))

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        
        
        # ignore own tweet and replies to tweet
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            return
        
        # check if it is a retweet
        if hasattr(tweet, 'retweeted_status'):
            logger.info(colored('This tweet is a retweet. Skipping..', 'yellow'))
            return

        logger.info((colored('{}'.format(tweet.user.name), 'green') + ': ' + colored('{}'.format(tweet.text), 'blue')))
        # Like tweet if hasn't been liked yet
        try:
            tweet.favorite()
        except Exception as error:
            logger.error("Failed to like tweet", exc_info=True)

        # Retweet tweet if hasn't been retweeted yet
        try:
            tweet.retweet()
        except Exception as error:
            logger.error("Failed to retweet", exc_info=True)

        
    def on_error(self, status):
        logger.error("Error detected. Status: {}".format(status))



tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=[keyword], languages=["en"])
