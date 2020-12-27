import os
import sys
import logging
import traceback
import twitter
from translate import translate_to
from last_tweet import get_last_tweet_id, put_last_tweet_id

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

orig_user_name = "PicardTips"

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token_key = os.getenv("ACCESS_TOKEN_KEY")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

# Get ID of last processed tweet.
try:
    last_tweet_id = get_last_tweet_id()
except:
    logger.error("Error occurred: \n Unable to get last tweet ID\n" +
                 traceback.format_exc() + "\nExitting!!!")
    sys.exit(1)

# Get all new tweets since last run.
try:
    logger.info("Getting all statues since last run.")
    statues = api.GetUserTimeline(screen_name=orig_user_name, since_id=last_tweet_id,
                                  include_rts=False, trim_user=True, exclude_replies=False)
except:
    logger.error("Error occurred: \n" +
                 traceback.format_exc() + "\nExitting!!!")
    sys.exit(1)

# Try to process the tweets, on error print it and ignore it.
for status in statues:
    try:
        # Get translated text in hindi
        translated_text = translate_to(status.text, "hi")
    except:
        logger.error("Error occurred: " + traceback.format_exc())
        continue
    try:
        # Post status update
        api.PostUpdate(status=translated_text, attachment_url="https://twitter.com/" +
                       orig_user_name + "/status/" + str(status.id))
    except:
        logger.error("Error occurred: " + traceback.format_exc())
        continue

# Update last tweet ID
if len(statues) > 0:
    try:
        put_last_tweet_id(str(statues[0].id))
    except:
        logger.error("Error occurred: \n Unable to update last tweet ID\n" +
                     traceback.format_exc() + "\nExitting!!!")
