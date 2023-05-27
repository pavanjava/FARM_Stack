from pymongo import MongoClient

db_connection = MongoClient("mongodb://localhost:27017")
db = db_connection["nobel_prize_db"]
collection = db["nobel_prize"]
