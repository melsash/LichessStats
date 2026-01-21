# Lichess Stats API

FastAPI backend service for retrieving and filtering chess games from Lichess
using OAuth2 (PKCE).  
Implemented as a technical test assignment.

## Features

- OAuth2 authentication via Lichess (PKCE)
- Fetch user games from Lichess API
- Filtering by:
  - game type (blitz / rapid / classical)
  - rated / casual games
  - date range (since / until)
  - limit
- Normalized game data for frontend usage

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- httpx
- Lichess API


## Setup & Run

 1. Clone repository
    git clone <>
    cd lichess-stats-api

 2. Create and activate virtual environment
 python -m venv .venv
    source .venv/bin/activate

 3. Install dependencies
    pip install -r requirements.txt

 4. Environment variables
  Create .env file in project root:
   LICHESS_CLIENT_ID=your_client_id
   LICHESS_REDIRECT_URI=http://127.0.0.1:8000/auth/callback

##Run application

    uvicorn app.main:app --reload

 Server will be available at: http://127.0.0.1:8000

##Authentication

 1.Open in browser: GET /auth/login

 2.Login via Lichess and allow access

 3.After redirect, access token is stored in memory 


 ##API Endpoints
 
  GET /games

    Example:/games?perfType=blitz&rated=true&limit=5

##Notes

Token storage is in-memory (simplified for test assignment)

Single-user mode (username is temporarily hardcoded)


#Possible Improvements

    Persistent token storage (Redis / DB)
    Multi-user support
    Cursor-based pagination
    Caching Lichess API responses
    Unit and integration tests
