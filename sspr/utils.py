import sys

from loguru import logger


def set_global_log_level(level: str):
    logger.remove()
    logger.add(sys.stdout, level=level)
