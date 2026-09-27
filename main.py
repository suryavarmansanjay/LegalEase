from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router

app = FastAPI(
    title="LegalEase - AI Legal Document Generator",
    version="1.0.0",
    description="Generates editable legal document drafts using Gemini."
)

# Allow the Streamlit frontend to call the FastAPI backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this to your frontend URL in production.
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "LegalEase API is running",
        "docs": "/docs"
    }

app.include_router(router)
