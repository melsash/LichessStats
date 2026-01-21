from typing import Optional


def extract_pgn_preview(pgn: Optional[str], moves_limit: int = 8) -> Optional[str]:
    """
    Возвращает короткий превью ходов из PGN (первые ~4 хода).
    """
    if not pgn:
        return None

    parts = pgn.split("\n\n")
    if len(parts) < 2:
        return None

    moves_part = parts[-1]
    moves = moves_part.split()
    return " ".join(moves[:moves_limit])


def normalize_game(game: dict, username: str) -> dict:
    players = game.get("players", {})

    if players.get("white", {}).get("user", {}).get("name") == username:
        opponent = players.get("black", {})
        color = "white"
    else:
        opponent = players.get("white", {})
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

    opening = None
    opening_data = game.get("opening")

    if isinstance(opening_data, dict):
        opening = opening_data.get("name")
    elif isinstance(opening_data, str):
        opening = opening_data

    return {
        "id": game.get("id"),
        "createdAt": game.get("createdAt"),
        "perf": game.get("perf"),
        "timeControl": game.get("clock"),
        "result": result,
        "termination": termination,
        "opening": opening,
        "opponent": {
            "username": opponent.get("user", {}).get("name"),
            "rating": opponent.get("rating"),
        },
        "url": f"https://lichess.org/{game.get('id')}",
    }
