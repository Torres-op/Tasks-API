import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME   = os.getenv("MONGO_DB",  "tasks_db")

client = MongoClient(MONGO_URL)

db = client[DB_NAME]

tasks_collection = db["tasks"]
