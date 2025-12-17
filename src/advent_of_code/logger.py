"""Logger."""

import logging
import sys


def get_logger(name: str, level: int | str | None = None) -> logging.Logger:
    """Get custom logger."""
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )

        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setFormatter(formatter)

        if level is None:
            level = "DEBUG"

        logger.setLevel(level)
        logger.addHandler(console_handler)
        logger.propagate = False

    return logger
