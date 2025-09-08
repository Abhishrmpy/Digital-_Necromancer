# backend/core/file_processor.py

import os
from pathlib import Path
from typing import List
import logging

from models.schemas import FileContent
from utils.logging_setup import logger

class FileProcessor:
    """Handles reading and processing files from a directory."""
    
    # Define valid file extensions we can process
    VALID_EXTENSIONS = {
        '.txt': 'Text File',
        '.py': 'Python Script', 
        '.md': 'Markdown',
        '.js': 'JavaScript',
        '.jsx': 'React JSX',
        '.html': 'HTML',
        '.css': 'CSS',
        '.java': 'Java',
        '.c': 'C Source',
        '.cpp': 'C++ Source',
        '.cs': 'C# Source',
        '.php': 'PHP',
        '.rb': 'Ruby',
        '.go': 'Go',
        '.rs': 'Rust',
        '.json': 'JSON',
        '.yaml': 'YAML',
        '.yml': 'YAML',
        '.xml': 'XML'
    }
    
    def __init__(self):
        logger.info("FileProcessor initialized")

    def process_directory(self, folder_path: str) -> List[FileContent]:
        """
        Read and process all valid files from the given directory.
        
        Args:
            folder_path: Absolute path to the folder to analyze
            
        Returns:
            List of FileContent objects with file contents and metadata
            
        Raises:
            ValueError: If the path doesn't exist or no readable files found
            Exception: For any other file reading errors
        """
        logger.info(f"Processing directory: {folder_path}")
        
        # Validate the path exists
        if not os.path.exists(folder_path):
            error_msg = f"Folder path '{folder_path}' does not exist."
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        if not os.path.isdir(folder_path):
            error_msg = f"Path '{folder_path}' is not a directory."
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        # Get all files in the directory
        try:
            all_items = os.listdir(folder_path)
        except PermissionError as e:
            error_msg = f"Permission denied accessing folder '{folder_path}': {e}"
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        processed_files = []
        
        for item in all_items:
            item_path = os.path.join(folder_path, item)
            
            # Skip directories, only process files
            if not os.path.isfile(item_path):
                logger.debug(f"Skipping directory: {item}")
                continue
            
            # Check if file has a valid extension
            file_extension = os.path.splitext(item)[1].lower()
            if file_extension not in self.VALID_EXTENSIONS:
                logger.debug(f"Skipping unsupported file type: {item}")
                continue
            
            # Process the file
            try:
                file_content = self._read_single_file(item_path, file_extension)
                processed_files.append(file_content)
                logger.info(f"Successfully processed: {item}")
                
            except Exception as e:
                logger.warning(f"Failed to process {item}: {e}")
                # Create an error entry but don't stop processing other files
                error_file = FileContent(
                    filename=item,
                    content="",
                    file_type=file_extension,
                    error=str(e),
                    success=False
                )
                processed_files.append(error_file)
        
        # Check if we found any processable files
        if not processed_files:
            error_msg = f"No readable files found in '{folder_path}'. Supported formats: {list(self.VALID_EXTENSIONS.keys())}"
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        logger.info(f"Successfully processed {len(processed_files)} files from {folder_path}")
        return processed_files

    def _read_single_file(self, file_path: str, file_extension: str) -> FileContent:
        """
        Read a single file and return its content with metadata.
        
        Args:
            file_path: Full path to the file
            file_extension: File extension for type identification
            
        Returns:
            FileContent object with file contents and metadata
        """
        try:
            # Read file content with proper encoding handling
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # For very large files, we might want to truncate
            max_length = 10000  # ~10k characters per file to avoid overwhelming the AI
            if len(content) > max_length:
                content = content[:max_length] + f"\n\n--- CONTENT TRUNCATED AT {max_length} CHARACTERS ---"
                logger.warning(f"Truncated large file: {os.path.basename(file_path)}")
            
            return FileContent(
                filename=os.path.basename(file_path),
                content=content,
                file_type=file_extension,
                success=True
            )
            
        except UnicodeDecodeError:
            # Handle binary files or wrong encodings
            error_msg = f"Cannot read file (likely binary or wrong encoding): {os.path.basename(file_path)}"
            logger.warning(error_msg)
            return FileContent(
                filename=os.path.basename(file_path),
                content="",
                file_type=file_extension,
                error=error_msg,
                success=False
            )
            
        except Exception as e:
            error_msg = f"Error reading file {os.path.basename(file_path)}: {str(e)}"
            logger.warning(error_msg)
            return FileContent(
                filename=os.path.basename(file_path),
                content="",
                file_type=file_extension,
                error=error_msg,
                success=False
            )

    def get_combined_content(self, processed_files: List[FileContent]) -> str:
        """
        Combine contents of successfully processed files into a single string.
        
        Args:
            processed_files: List of FileContent objects
            
        Returns:
            Combined content string with file headers
        """
        combined_text = ""
        
        for file_content in processed_files:
            if file_content.success and file_content.content.strip():
                combined_text += f"\n\n--- {file_content.filename} ({self.VALID_EXTENSIONS.get(file_content.file_type, 'File')}) ---\n\n"
                combined_text += file_content.content
        
        return combined_text.strip()

# Create a singleton instance for use throughout the application
file_processor = FileProcessor()