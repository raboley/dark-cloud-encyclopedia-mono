import os
import json
import requests
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import tweepy

# Load Twitter API credentials from environment variables
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Initialize Twitter API client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def get_datetime_no_spaces():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def image_is_new(file_name, list_of_downloaded_images):
    return file_name not in list_of_downloaded_images

def get_already_downloaded(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return set(os.listdir(output_folder))

def download_image(media_url, output_folder):
    file_name = os.path.basename(media_url)
    response = requests.get(media_url)
    if response.status_code == 200:
        with open(os.path.join(output_folder, file_name), 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download: {file_name}")

def fetch_media_urls(username_or_hashtag, num_tweets, include_rts, exclude_replies):
    media_urls = []
    query = f"from:{username_or_hashtag} has:images"
    if not include_rts:
        query += " -is:retweet"
    if exclude_replies:
        query += " -is:reply"

    tweets = client.search_recent_tweets(query=query, tweet_fields=['attachments'], expansions=['attachments.media_keys'], media_fields=['url'], max_results=num_tweets)
    if tweets.data:
        media_keys = [media.media_key for media in tweets.includes['media']]
        for tweet in tweets.data:
            if 'attachments' in tweet:
                for media_key in tweet.attachments['media_keys']:
                    if media_key in media_keys:
                        media_url = next(media.url for media in tweets.includes['media'] if media.media_key == media_key)
                        media_urls.append(media_url)
    return media_urls

def main(arguments):
    username_or_hashtag = arguments['username_or_hashtag']
    include_rts = arguments['retweets']
    exclude_replies = arguments['replies']
    num_tweets = int(arguments['num'])
    output_folder = arguments['output_folder']

    list_of_downloaded_images = get_already_downloaded(output_folder)
    media_urls = fetch_media_urls(username_or_hashtag, num_tweets, include_rts, exclude_replies)

    with ThreadPoolExecutor() as executor:
        for media_url in media_urls:
            file_name = os.path.basename(media_url)
            if image_is_new(file_name, list_of_downloaded_images):
                executor.submit(download_image, media_url, output_folder)

if __name__ == '__main__':
    event = {
        "username_or_hashtag": "cloud_images",
        "num": "3",
        "retweets": False,
        "replies": False,
        "output_folder": "archive/"
    }
    main(event)
