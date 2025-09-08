# backend/models/schemas.py

from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class HistoricalFigure(str, Enum):
    """Enumeration of available historical figures for validation."""
    ALAN_TURING = "Alan Turing"
    LEONARDO_DA_VINCI = "Leonardo da Vinci"
    MARIE_CURIE = "Marie Curie"
    ALBERT_EINSTEIN = "Albert Einstein"
    NIKOLA_TESLA = "Nikola Tesla"
    ISAAC_NEWTON = "Isaac Newton"
    ARISTOTLE = "Aristotle"
    SUN_TZU = "Sun Tzu"

class AnalysisRequest(BaseModel):
    """Request model for the analysis endpoint."""
    folder_path: str = Field(
        ...,
        description="The absolute path to the folder containing files to analyze.",
        example="C:/Users/Developer/my_project"
    )
    historical_figure: HistoricalFigure = Field(
        ...,
        description="The name of the historical figure to embody."
    )

class FileContent(BaseModel):
    """Represents the content of a processed file with metadata."""
    filename: str
    content: str
    file_type: str
    error: Optional[str] = None
    success: bool = True

class AnalysisResponse(BaseModel):
    """Response model for a successful analysis."""
    analysis: str
    status: str = "success"
    model_used: str = "gpt-oss-20b"
    processed_files: List[FileContent] = []

class ErrorResponse(BaseModel):
    """Standardized error response model."""
    detail: str
    status: str = "error"
    error_code: Optional[str] = None

class HealthCheckResponse(BaseModel):
    """Response model for health check endpoint."""
    status: str = "healthy"
    service: str = "digital-necromancer-api"
    version: str = "1.0.0"