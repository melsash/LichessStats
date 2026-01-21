from fastapi import APIRouter, HTTPException
from app.core.auth_storage import tokens

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
async def get_current_user():
    access_token = tokens.get("access_token")

    if not access_token:
        raise HTTPException(status_code=401, detail="Пользователь не авторизован")

    return {
        "username": "h4nzarick",
        "status": "authorized"
    }
