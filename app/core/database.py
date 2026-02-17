from pymongo import MongoClient
from app.core.config import settings

"""
Database layer should ONLY consume settings,
never read environment variables directly.
"""

# create mongodb client
client = MongoClient(settings.MONGO_URI)

# get database
db = client[settings.DATABASE_NAME]


def get_database():
    """
    Returns MongoDB database instance.
    """
    return db