import sys
import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import create_tweets
from create_anime_quotes import create_anime_tweet
import time

FILE_NAME = 'last_seen.txt'


def read_last_seen():
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def write_last_seen(id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(id))
    file_write.close()
    return


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print('Authentication Successful')
    except:
        print('Error while authenticating API')
        sys.exit(1)


    def reply():
        # tweet = create_tweets.create_tweet()
        lastSeen = read_last_seen()
        my_tweets = api.mentions_timeline(since_id=lastSeen)

        for tweet_obj in reversed(my_tweets):
            print(tweet_obj._json['id'])
            quote = create_anime_tweet()
            user = '@'+tweet_obj._json['user']['screen_name']
            print('*** user ', user)
            api.update_status(user + ' ' + quote, tweet_obj._json['id'])
            write_last_seen(tweet_obj._json['id'])

    while True:
        reply()
        time.sleep(5)


