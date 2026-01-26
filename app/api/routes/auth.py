from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import UserCreate
from app.core.security import (hash_password, verify_password, create_access_token)
from app.services.db_collections import users_collection
from datetime import datetime

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(user: UserCreate):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    user_dict["role"] = "user"
    user_dict["created_at"] = datetime.utcnow()

    users_collection.insert_one(user_dict)

    return {"message": "User registered successfully"}


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    password = form_data.password

    # ✅ Manual guard for bcrypt limit
    if len(password.encode("utf-8")) > 72:
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials"
        )

    user = users_collection.find_one({"email": form_data.username})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user["_id"])})

    return {
        "access_token": token,
        "token_type": "bearer"
    }