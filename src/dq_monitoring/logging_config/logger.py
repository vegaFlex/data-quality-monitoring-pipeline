import logging
from pathlib import Path


LOG_FILE_PATH = Path("logs") / "pipeline.log"


def get_logger() -> logging.Logger:
    logger = logging.getLogger("dq_pipeline")

    if logger.handlers:
        return logger

    LOG_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(LOG_FILE_PATH, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.propagate = False

    return logger
