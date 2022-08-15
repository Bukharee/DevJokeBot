import os
import tweepy
from twitter_secret import tweeter_secrets as ts
from flask import Flask
from . import db



consumer_key = ts.CONSUMER_KEY
consumer_secret = ts.CONSUMER_SECRET

access_token = ts.ACCESS_TOKEN
access_secret = ts.ACESS_SECRET

#authentication 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


app = Flask(__name__, instance_relative_config=True)

def create_app(test_config=None):
    # create and configure the app
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    db.init_app(app)
    return app





