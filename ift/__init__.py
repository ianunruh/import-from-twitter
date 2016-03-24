import json
from types import ModuleType

import tweepy

CONFIG = {}

def configure(path='config.json'):
    with open(path) as fp:
        CONFIG.update(json.load(fp))

def create_module(code):
    module = ModuleType('imported_from_twitter_yo')
    exec(code, module.__dict__)
    return module

def import_from_twitter(tweet_id):
    auth = tweepy.OAuthHandler(CONFIG['consumer_key'], CONFIG['consumer_secret'])
    auth.set_access_token(CONFIG['access_token'], CONFIG['access_token_secret'])

    api = tweepy.API(auth)

    status = api.get_status(tweet_id)

    return create_module(status.text)
