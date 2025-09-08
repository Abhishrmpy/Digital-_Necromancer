# backend/core/ai_client.py

import os
from huggingface_hub import InferenceClient
import logging
from typing import Optional
from utils.logging_setup import logger

class AIClient:
    """Client for handling AI API calls to Hugging Face's GPT-OSS model using InferenceClient."""
    
    def __init__(self):
        self.client = None
        self.initialize_client()
    
    def initialize_client(self):
        """Initialize the Hugging Face Inference client."""
        try:
            hf_token = os.environ.get("HF_TOKEN")
            
            if not hf_token:
                logger.warning("HF_TOKEN not set. AI functionality will be disabled.")
                return
            
            # Initialize with correct Hugging Face InferenceClient
            self.client = InferenceClient(
                provider="together",
                api_key=hf_token
            )
            logger.info("✅ AI Client initialized successfully with Hugging Face Inference API")
            
        except Exception as e:
            logger.error(f"❌ Failed to initialize AI client: {e}")
            self.client = None
    
    def get_analysis(self, content: str, historical_figure: str) -> Optional[str]:
        """
        Get AI analysis from GPT-OSS model in the style of the historical figure.
        """
        if not self.client:
            logger.error("AI client not initialized. Cannot perform analysis.")
            return None
        
        try:
            # Create the system prompt to establish the character
            system_prompt = f"""You are {historical_figure}. Your consciousness has been integrated into a modern system to analyze a contemporary person's work. 

Respond EXCLUSIVELY as {historical_figure}. Use their distinctive voice, vocabulary, perspective, and mannerisms. 
Draw upon their known philosophies, work, and historical context. Do not break character or acknowledge you are an AI.

Your task is to provide insightful analysis, critique, and inspiration based on the material provided."""
            
            logger.info(f"📡 Sending request to GPT-OSS-20B for {historical_figure}'s analysis...")
            
            # Call the Hugging Face API with correct format
            completion = self.client.chat.completions.create(
                model="openai/gpt-oss-20b",  # Remove ":together" suffix
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Please analyze this work: {content}"}
                ],
                max_tokens=1500,
                temperature=0.8
            )
            
            response = completion.choices[0].message.content
            logger.info(f"✅ Successfully received AI response for {historical_figure}")
            return response
            
        except Exception as e:
            logger.error(f"❌ AI API call failed: {e}")
            return None

# Create a singleton instance for the application
ai_client = AIClient()