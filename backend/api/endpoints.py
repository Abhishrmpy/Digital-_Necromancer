# backend/api/endpoints.py


import os
from fastapi import APIRouter, HTTPException
from typing import List

from httpcore import request
from models.schemas import AnalysisRequest, AnalysisResponse, ErrorResponse, FileContent
from core.file_processor import file_processor
from core.ai_client import ai_client  # <-- ADD THIS IMPORT
from utils.logging_setup import logger

# Create a router for API endpoints
router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse, responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}})
async def analyze_files(request: AnalysisRequest):
    """
    Main endpoint to analyze files using a historical figure's perspective.
    
    - **folder_path**: Absolute path to the folder containing files to analyze
    - **historical_figure**: Which historical figure's perspective to use for analysis
    """
    logger.info(f"Analysis request received for {request.historical_figure} on path: {request.folder_path}")
    
    try:
        # 1. Process files from the provided directory
        processed_files = file_processor.process_directory(request.folder_path)
        
        # 2. Combine the content for AI analysis
        combined_content = file_processor.get_combined_content(processed_files)
        
        logger.info(f"Successfully processed {len(processed_files)} files. Total content length: {len(combined_content)} characters")
        

        # 3. Get AI analysis (NEW - AI INTEGRATION)
        ai_response = None

        # DEBUG: Add these 2 lines - they will show us what's happening
        print(f"🔍 DEBUG: ai_client.client = {ai_client.client}")
        print(f"🔍 DEBUG: HF_TOKEN present = {bool(os.environ.get('HF_TOKEN'))}")

        if ai_client.client:  # Check if AI client is initialized (HF_TOKEN is set)
            logger.info(f"Requesting AI analysis from {request.historical_figure.value}")
            ai_response = ai_client.get_analysis(combined_content, request.historical_figure.value)
            # DEBUG: Add these 2 lines to see the response
            print(f"🔍 DEBUG: ai_response type = {type(ai_response)}")
            if ai_response:
                print(f"🔍 DEBUG: ai_response content = {ai_response[:200]}...")  # First 200 chars
            else:
                print("🔍 DEBUG: ai_response is None")
        else:
            logger.warning("AI client not available - skipping AI analysis")
            print("🔍 DEBUG: AI client is None - check initialization")
        
        # 4. Return the response (UPDATED)
        return AnalysisResponse(
            analysis=ai_response or f"✅ Processed {len(processed_files)} files. AI analysis unavailable - check HF_TOKEN configuration.",
            processed_files=processed_files,
            status="success" if ai_response else "partial_success"
        )
        
    except ValueError as e:
        # Handle file/directory not found errors
        logger.warning(f"File processing error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
        
    except Exception as e:
        # Handle any other errors
        logger.error(f"Unexpected error during file processing: {e}")
        raise HTTPException(
            status_code=500, 
            detail=f"An unexpected error occurred: {str(e)}"
        )