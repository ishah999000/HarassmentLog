import tweepy
import json
import random
import schedule
import time
import os
from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(
    bearer_token=os.getenv("X_BEARER_TOKEN"),
    consumer_key=os.getenv("X_API_KEY"),
    consumer_secret=os.getenv("X_API_SECRET"),
    access_token=os.getenv("X_ACCESS_TOKEN"),
    access_token_secret=os.getenv("X_ACCESS_SECRET")
)

def post_tweet():
    with open("ha_quotes.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    random_chapter = random.choice(list(data.keys()))
    random_sentence = random.choice(data[random_chapter])

    client.create_tweet(text=f"{random_chapter}\n{random_sentence}")
    print(f"Posted: {random_chapter} - {random_sentence}")

schedule.every(3).hours.do(post_tweet)

print("Bot is running...")
post_tweet()  # posts immediately on startup too
while True:
    schedule.run_pending()
    time.sleep(60)