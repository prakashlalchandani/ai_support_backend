from fastapi import FastAPI
from app.api.routes import auth, users, tickets, messages, admin
from app.core.database import get_database
from app.core.config import settings
from app.services.db_collections import users_collection

app = FastAPI(title=settings.APP_NAME)

@app.get("/")
def root():
    return {"message": "Welcome to AI Support Backend"}

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(admin.router)
app.include_router(tickets.router)
app.include_router(messages.router)