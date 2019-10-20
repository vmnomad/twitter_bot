import tweepy
import sys
import logging
import os

# create logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Check authentication
def create_api():

    try:
        consumer_key = os.getenv("CONSUMER_KEY")
        consumer_secret = os.getenv("CONSUMER_SECRET")
        access_token = os.getenv("ACCESS_TOKEN")
        access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    except:
        logger.error('Failed to get keys from env variables', exc_info=True)
        sys.exit('Exiting..')

    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    except:
        logger.error('Failed create API', exc_info=True)
        sys.exit('Exiting..')

    try:
        api.verify_credentials()
        logger.info("Authentication OK. API is created")
        return api
    except Exception as error:
        logger.error("Error during authentication: {}".format(error))
        logger.info('Please ensure ENV variables are set correctly on the host system or in the dockerfile')
        sys.exit('Exiting..')

def get_keyword():
    try:
        return os.getenv("KEYWORD")
    except Exception as error:
        logger.error("Error during authentication: {}".format(error))
        sys.exit('Exiting..')