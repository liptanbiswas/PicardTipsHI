import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

firebase_admin.initialize_app()
db = firestore.client()
doc_ref = db.collection("last_processed_tweet").document("1")


def get_last_tweet_id():
    doc = doc_ref.get()
    return(doc.get("tweet_id"))


def put_last_tweet_id(tweet_id):
    doc_ref.update({"tweet_id": tweet_id})
