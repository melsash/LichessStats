from fastapi import FastAPI
from app.api import auth, users, games

app = FastAPI(title="Lichess Stats API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(games.router)  

@app.get("/")
async def healthcheck():
    return {"status": "ok"}
