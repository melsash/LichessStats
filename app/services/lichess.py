import httpx
from typing import Optional

LICHESS_API_BASE = "https://lichess.org/api"

def normalize_game(game: dict, username: str) -> dict:
    players = game.get("players", {})

    if players.get("white", {}).get("user", {}).get("name") == username:
        opponent = players["black"]
        color = "white"
    else:
        opponent = players["white"]
        color = "black"

    if game.get("winner") == color:
        result = "win"
    elif game.get("winner") is None:
        result = "draw"
    else:
        result = "loss"

    status_map = {
        "mate": "mate",
        "resign": "resign",
        "timeout": "time",
        "draw": "draw",
        "stalemate": "draw",
    }

    termination = status_map.get(game.get("status"), "unknown")

    
    preview_moves = None
    pgn = game.get("pgn")
    if pgn:
        moves_part = pgn.split("\n\n")[-1]
        preview_moves = " ".join(moves_part.split()[:8])  # ~4 хода

    return {
        "id": game.get("id"),
        "createdAt": game.get("createdAt"),
        "perf": game.get("perf"),
        "timeControl": game.get("clock"),
        "result": result,
        "termination": termination,
        "opening": game.get("opening", {}).get("name"),
        "preview": preview_moves,  
        "opponent": {
            "username": opponent.get("user", {}).get("name"),
            "rating": opponent.get("rating"),
        },
        "url": f"https://lichess.org/{game.get('id')}",
    }



async def get_user_games(
    username: str,
    access_token: str,
    max_games: int = 10,
    perf_type: Optional[str] = None,
    rated: Optional[bool] = None,
    since: Optional[int] = None,
    until: Optional[int] = None,
) -> list[dict]:
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/x-ndjson",
    }

    params = {
        "max": max_games,
        "moves": False,
        "opening": True,
        "clocks": True,
        "pgnInJson": True,
    }

    if perf_type:
        params["perfType"] = perf_type
    if rated is not None:
        params["rated"] = rated
    if since:
        params["since"] = since
    if until:
        params["until"] = until

    url = f"{LICHESS_API_BASE}/games/user/{username}"

    games: list[dict] = []

    async with httpx.AsyncClient(timeout=20) as client:
        async with client.stream("GET", url, headers=headers, params=params) as response:
            async for line in response.aiter_lines():
                if line:
                    raw_game = httpx.Response(200, text=line).json()
                    games.append(normalize_game(raw_game, username))

    return games
