from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Lichess Stats API"

    
    LICHESS_CLIENT_ID: str = "demo"
    LICHESS_CLIENT_SECRET: str = "demo"
    LICHESS_REDIRECT_URI: str = "http://localhost:8000/auth/callback"

settings = Settings()
