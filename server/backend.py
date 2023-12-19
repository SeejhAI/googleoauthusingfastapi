from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from server.utils.rate_limit import rate_limited
from server.routers import (
    user_router, 
    auth
    )
app = FastAPI(title="Google Auth for FastAPI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.include_router(user_router.router)
app.include_router(auth.router)

@app.get("/ping")
@rate_limited(max_calls=10, time_frame=30)
def health_check(request: Request):
    """Health check."""

    return {"message": "Hello I am working!"}

@app.get("/")
def intro():
    """
    This Endpoint for intro to this backend
    """
    return {"message": "Welcome to the oauth Backend"}

## trying to add firebase auth in fastapi 
@app.post("/signup")
async def create_an_account():
    pass