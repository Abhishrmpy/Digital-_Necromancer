# backend/utils/logging_setup.py

import logging
import sys
from pathlib import Path

def setup_logging():
    """
    Configures application-wide logging.
    Logs will go to both the console and a file.
    """
    # Create a logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Create a formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Console handler (shows output in terminal)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    
    # File handler (saves logs to file)
    file_handler = logging.FileHandler(
        log_dir / "digital_necromancer.log",
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    
    # Get the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
    
    # Create a logger for this specific module
    logger = logging.getLogger(__name__)
    logger.info("Logging setup complete.")
    
    return logger

# Create a module-level logger
logger = logging.getLogger(__name__)