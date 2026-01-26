from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# read values from .env
MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")


if not MONGO_URL or not DATABASE_NAME:
    raise ValueError("MONGO_URI OR DATABASE_NAME not set in .env file")

# create mongodb client
client = MongoClient(MONGO_URL)

# get database
db = client[DATABASE_NAME]

def get_database():
    """
    Returns MongoDB database instance.
    Use this function to access DB across the app.
    """
    return db