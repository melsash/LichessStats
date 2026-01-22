# Lichess Stats — Fullstack App

Fullstack web application for retrieving and analyzing chess games from Lichess
using OAuth2 (PKCE).

Built as a technical test assignment.

## Features

Authentication:

   OAuth2 authentication via Lichess (PKCE)

   Secure login via official Lichess API

   Session-based auth (cookies)

Game Data

   Fetch user games from Lichess

   Normalized backend response for frontend usage

   Direct links to games on lichess.org

Filters

   Game type: Blitz / Rapid / Classical

   Rated / Casual

   Games limit (5 / 10 / 20 / 50)

Frontend

   React-based UI

   Automatic game loading after login

   Loading & empty states

   Responsive dark UI

## Tech Stack

Backend:
   Python 3.11
   FastAPI
   Uvicorn
   httpx
   Lichess API
   OAuth2 (PKCE)
Frontend:
   React (Vite)
   JavaScript (ES6+)
   CSS (custom styles)
   Fetch API


## Project Structure
backend-app/api/auth/games
frontend/src/api/components/pages/package.json

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

## Run application

    uvicorn app.main:app --reload

 Server will be available at: http://127.0.0.1:8000

## Frontend Setup
cd frontend
npm install
npm run dev

Frontend will be available at: http://localhost:5173
## Authentication Flow

 1.Open frontend in browser

 2.Click “Login via Lichess”

 3.Authorize application on lichess.org
 
 4.After redirect, session is established
 
 5.Games are loaded automatically

 ##API Endpoints
 
  GET /games

    Example:/games?perfType=blitz&rated=true&limit=5

## Notes

Token storage is in-memory (simplified for test assignment)

Single-user mode (username is temporarily hardcoded)

No database is used


# Possible Improvements

    Persistent token storage (Redis / DB)
    Multi-user support
    Cursor-based pagination
    Caching Lichess API responses
    Unit and integration tests
    Docker setup
    Charts and statistics (win rate, ratings)

# Project Status
Completed
Ready for demo, review.