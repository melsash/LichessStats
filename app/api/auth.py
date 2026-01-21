from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode
import httpx
import secrets
import hashlib
import base64

from app.core.auth_storage import tokens
from app.core.config import settings

router = APIRouter()

LICHESS_AUTHORIZE_URL = "https://lichess.org/oauth"
LICHESS_TOKEN_URL = "https://lichess.org/api/token"


pkce_store = {}


def generate_pkce_pair():
    code_verifier = secrets.token_urlsafe(64)
    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode()).digest()
    ).decode().rstrip("=")
    return code_verifier, code_challenge


@router.get("/login")
def login():
    code_verifier, code_challenge = generate_pkce_pair()
    pkce_store["verifier"] = code_verifier

    params = {
        "response_type": "code",
        "client_id": settings.LICHESS_CLIENT_ID,
        "redirect_uri": settings.LICHESS_REDIRECT_URI,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
    }

    url = f"{LICHESS_AUTHORIZE_URL}?{urlencode(params)}"
    return RedirectResponse(url)


@router.get("/callback")
async def callback(request: Request):
    code = request.query_params.get("code")

    if not code:
        raise HTTPException(status_code=400, detail="Отсутствует code")

    code_verifier = pkce_store.get("verifier")
    if not code_verifier:
        raise HTTPException(status_code=400, detail="PKCE verifier не найден")

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": settings.LICHESS_REDIRECT_URI,
        "client_id": settings.LICHESS_CLIENT_ID,
        "code_verifier": code_verifier,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(LICHESS_TOKEN_URL, data=data)

    if response.status_code != 200:
        raise HTTPException(
            status_code=400,
            detail="Ошибка авторизации через Lichess"
        )

    token_data = response.json()
    tokens["access_token"] = token_data["access_token"]

    pkce_store.clear()

    return {
        "message": "Успешная авторизация через Lichess",
        "token_type": token_data["token_type"],
        "expires_in": token_data["expires_in"],
    }


@router.post("/logout")
def logout():
    tokens.clear()
    pkce_store.clear()
    return {"message": "Вы вышли из системы"}
