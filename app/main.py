from fastapi import FastAPI
from app.api import auth, users, games
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Lichess Stats API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(games.router)  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def healthcheck():
    return {"status": "ok"}
