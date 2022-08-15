from flaskr.__init__ import app, api
import pandas as pd
import requests
endpoint = "https://raw.githubusercontent.com/15Dkatz/official_joke_api/master/jokes/index.json"


@app.route('/test')
def tweet_test():
    tweet = "this is testing tweet"
    try:
        tweeting = api.update_status(tweet)
    except:
        response = requests.get(endpoint)
        print(type(response.json()))
        return str(response.json())