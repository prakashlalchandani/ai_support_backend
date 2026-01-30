from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# read values from .env
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")


if not MONGO_URI or not DATABASE_NAME:
    raise ValueError("MONGO_URI OR DATABASE_NAME not set in .env file")

# create mongodb client
client = MongoClient(MONGO_URI)

# get database
db = client[DATABASE_NAME]

def get_database():
    """
    Returns MongoDB database instance.
    Use this function to access DB across the app.
    """
    return db