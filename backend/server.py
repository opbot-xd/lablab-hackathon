from flask import Flask, request, jsonify
import datetime
import uuid
import threading
from supabase import create_client
from script import script
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)


def process_tweet(query, mood, tweet_uuid):
    script(query, mood, tweet_uuid)


@app.route("/get_data", methods=["POST"])
def get_data():
    tweet = request.json.get("tweet")
    mood = request.json.get("mood")
    tweet_uuid = str(uuid.uuid4())
    supabase_client.table("tweets").insert({
        "uuid": tweet_uuid,
        "tweet": "loading...",
        "pending": True
    }).execute()

    threading.Thread(target=process_tweet, args=(tweet, mood, tweet_uuid)).start()
    return jsonify({"uuid": tweet_uuid})

@app.route("/status", methods=["GET"])
def check_status():
    tweet_uuid = request.headers.get("uuid")
    response = supabase_client.table("tweets").select("*").eq("uuid", tweet_uuid).execute()
    if response.data:
        return jsonify(response.data[0])
    else:
        return jsonify({"error": "Tweet not found"}), 404

if __name__ == "__main__":
    app.run()
