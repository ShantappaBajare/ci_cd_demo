# utils/logger.py
import logging
import os
from datetime import datetime

def get_logger(test_name: str = "test_suite"):
    """
    Returns a logger that writes to:
    1. Console
    2. A file in logs/ folder with timestamp and test name
    """

    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    # Timestamped log file per test run
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"{test_name}_{timestamp}.log")

    logger = logging.getLogger(test_name)
    logger.setLevel(logging.INFO)

    # Avoid adding multiple handlers if logger is called multiple times
    if not logger.handlers:
        # File Handler
        fh = logging.FileHandler(log_file)
        fh.setFormatter(logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        ))
        logger.addHandler(fh)

        # Console Handler
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        ))
        logger.addHandler(ch)

    return logger