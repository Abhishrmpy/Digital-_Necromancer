# backend/main.py

import os
import sys
from pathlib import Path

# Add the current directory to Python path so relative imports work
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Import our modules using absolute paths
from api.endpoints import router as analysis_router
from utils.logging_setup import logger, setup_logging

# Setup logging first thing
setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan events for startup and shutdown.
    This is the professional way to handle app lifecycle in FastAPI.
    """
    # Startup
    logger.info("Digital Necromancer API is starting up...")
    
    # Check if our crucial environment variable is set
    if not os.environ.get("HF_TOKEN"):
        logger.error("CRITICAL: HF_TOKEN environment variable is not set. The AI functionality will fail.")
    else:
        logger.info("HF_TOKEN environment variable found.")
    
    yield  # The application runs here
    
    # Shutdown
    logger.info("Digital Necromancer API is shutting down.")

# Initialize FastAPI app with lifespan
app = FastAPI(
    title="Digital Necromancer API",
    description="An API to conjure the wisdom of historical figures for code and project analysis.",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS - Essential for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default port
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include our API router
app.include_router(analysis_router, prefix="/api/v1", tags=["analysis"])

# Basic root endpoint
@app.get("/")
async def root():
    """Root endpoint that provides basic API information."""
    return {
        "message": "Welcome to the Digital Necromancer API",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "operational"
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring API status."""
    return {"status": "healthy", "service": "digital-necromancer-api"}