from flask import Flask
import pymongo
import os


app = Flask(__name__)
connection = pymongo.MongoClient(
    os.getenv('STEAM_MONGODB_HOST'),
    int(os.getenv('STEAM_MONGODB_PORT'))
)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def get_db():
    db = connection.myFirstMB
    return db

@app.route("/test")
def get_data():
    print('hej')
    db = get_db()
    return "hej"
    return db.SteamTopListItem.find_one()
