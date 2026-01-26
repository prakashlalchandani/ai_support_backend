from fastapi import Depends, APIRouter
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me")
def read_me(current_user=Depends(get_current_user)):
    return {
        "email": current_user["email"],
        "role": current_user["role"]
    }