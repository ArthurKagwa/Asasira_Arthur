import tweepy
import random
import logging
import datetime
import time
import os
import dotenv
from together import Together
from requests_oauthlib import OAuth1
import requests

# Load environment variables from .env file
dotenv.load_dotenv('/Users/arthur/recess/Asasira_Arthur/.env')



# Load Together AI API key
TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')
MODEL = os.getenv('MODEL')

auth = OAuth1(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET"),
    os.getenv("ACCESS_TOKEN"),
    os.getenv("ACCESS_SECRET")
)

# Graded Assignment (20): Create an AI agent that automates tasks of creating posts on social media platforms # like X.com (formerly Twitter)using Python.

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("climate_tweet_bot.log"),
        logging.StreamHandler()
    ]
)
client = Together(api_key=TOGETHER_API_KEY)

def generate_climate_tweet():
    prompt = (
        "Write a short, engaging tweet (max 280 characters) about climate action, sustainability, or environmental protection. "
        "Make it positive, actionable, and suitable for a general audience. Maintain an African context."
    )
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        tweet = response.choices[0].message.content.strip()
        tweet = tweet[:280]
        logging.info(f"Generated tweet: {tweet}")
        return tweet
    except Exception as e:
        logging.error(f"Error generating tweet: {e}")
        return None

def post_tweet(tweet):
    if not tweet:
        logging.warning("No tweet text provided. Skipping post.")
        return

    url = "https://api.twitter.com/2/tweets"
    payload = {"text": tweet}
    try:
        resp = requests.post(url, auth=auth, json=payload)
        if resp.status_code == 201:
            logging.info(f"Tweet posted successfully: {tweet}")
        else:
            logging.error(f"Failed to post tweet: {resp.status_code} - {resp.text}")
    except Exception as e:
        logging.error(f"Exception while posting tweet: {e}")

# 2025-07-01 15:17:08,435 - ERROR - Failed to post tweet: 403 - {"title":"Forbidden","status":403,"detail":"Your client app is not configured with the appropriate oauth1 app permissions for this endpoint.","type":"https://api.twitter.com/2/problems/oauth1-permissions"}

# due to need to upgrade

if __name__ == "__main__":
    while True:
        tweet = generate_climate_tweet()
        post_tweet(tweet)
        logging.info("Sleeping for 6 hours before next tweet.")
        time.sleep(6 * 60 * 60)

