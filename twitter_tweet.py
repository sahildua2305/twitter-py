import twitter

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''

class Twitter():
    def __init__(self, access_token_secret = ACCESS_TOKEN_SECRET, access_token_key = ACCESS_TOKEN_KEY, consumer_secret = CONSUMER_SECRET, consumer_key = CONSUMER_KEY):
        self.api = twitter.Api(access_token_secret = access_token_secret, access_token_key=access_token_key, consumer_secret=consumer_secret, consumer_key=consumer_key)

    def post_tweet(self, tweet_text):
        self.api.PostUpdate(tweet_text)

text = raw_input()
twitter_client = Twitter()

twitter_client.post_tweet(text)
