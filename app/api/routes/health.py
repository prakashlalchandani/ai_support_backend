from fastapi import APIRouter
from app.services.db_collections import tickets_collection

router = APIRouter()

@router.get("/health")
def health_check():
    try:
        tickets_collection.find_one()
        return {"status": "ok", "db": "connected"}
    except Exception:
        return {"status": "degraded", "db": "down"}
