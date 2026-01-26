from fastapi import FastAPI
from app.api.routes import auth, users, tickets, messages
from app.core.database import get_database
from app.core.config import settings
from app.services.db_collections import users_collection

app = FastAPI(title=settings.APP_NAME)

@app.get("/")
def root():
    return {"message": "Welcome to AI Support Backend"}

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tickets.router)
app.include_router(messages.router)

"""@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.APP_NAME
    }

@app.get("/db-test")
def db_test():
    db = get_database()
    collections = db.list_collection_names()
    return {
        "status": "connected",
        "collections": collections
    }

@app.get("/test-user-collection")
def test_users():
    return "Collection {user_collection.name}"""