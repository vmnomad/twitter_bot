# My Very First Twitter Bot

This bot will use configured keyword to like and retweet the tweets that contain the keyword

It was built Tweepy and following this [guide](https://realpython.com/twitter-bot-python-tweepy/)

The logic of the code int this blog post was slightly updated to avoid ignoring any retweets

**The bot requires the following ENV variables for authentication:**

- CONSUMER_KEY
- CONSUMER_SECRET
- ACCESS_TOKEN
- ACCESS_TOKEN_SECRET

**Another ENV variable is required to set the keyword for tweets:**
- KEYWORD

**To run the bot in the container update the above mentioned variables in the dockerfile before building the image**
