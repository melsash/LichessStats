from fastapi import APIRouter, HTTPException
from typing import Optional

from app.core.auth_storage import tokens
from app.services.lichess import get_user_games
from app.utils.normalizers import normalize_game


router = APIRouter(prefix="/games", tags=["games"])


@router.get("/")
async def user_games(
    limit: int = 10,
    perfType: Optional[str] = None,
    rated: Optional[bool] = None,
    since: Optional[int] = None,
    until: Optional[int] = None,
):
    access_token = tokens.get("access_token")

    if not access_token:
        raise HTTPException(status_code=401, detail="Не авторизованы")

    username = "h4nzarick"

    raw_games = await get_user_games(
        username=username,
        access_token=access_token,
        max_games=limit,
        perf_type=perfType,
        rated=rated,
        since=since,
        until=until,
    )

    normalized_games = [
        normalize_game(game, username)
        for game in raw_games
    ]

    return {
        "count": len(normalized_games),
        "games": normalized_games,
    }
