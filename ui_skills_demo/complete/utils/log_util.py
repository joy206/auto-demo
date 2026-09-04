"""
自定义logger
"""
import logging
from datetime import datetime
from pathlib import Path


def setup_logger():

    swag_logger = logging.getLogger('swag_logger')
    swag_logger.setLevel(logging.DEBUG)
    swag_logger.handlers.clear()
    swag_logger.propagate= False

    console_handler = logging.StreamHandler()

    log_dir = Path(__file__).resolve().parent.parent / "logs"
    log_dir.mkdir(exist_ok=True)
    log_name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".log"
    log_file = log_dir / log_name

    file_handler = logging.FileHandler(log_file, encoding="utf-8")

    formatter = logging.Formatter(
        "%(filename)s - %(levelname)s - %(message)s",
        "%Y_%m_%d %H:%M:%S"
    )

    console_handler.setFormatter(file_handler)
    file_handler.setFormatter(formatter)

    swag_logger.addHandler(console_handler)
    swag_logger.addHandler(file_handler)

    return swag_logger


swag_logger = setup_logger()