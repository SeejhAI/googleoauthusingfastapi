from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Google Auth for FastAPI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
@app.get("/ping")
def health_check():
    """Health check."""

    return {"message": "Hello I am working!"}

@app.get("/")
def intro():
    """
    This Endpoint for intro to this backend
    """
    return {"message": "Welcome to the oauth Backend"}