from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from app.core.limiter import limiter
from app.api.routes import auth, users, tickets, messages, admin, analytics, health
from app.core.database import get_database
from app.core.config import settings
from app.services.db_collections import users_collection

app = FastAPI(title=settings.APP_NAME)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/")
def root():
    return {"message": "Welcome to AI Support Backend"}

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(admin.router)
app.include_router(tickets.router)
app.include_router(messages.router)
app.include_router(analytics.router)
app.include_router(health.router)