import logging
import sys


class Logger:
    def __init__(self, log_level: str):
        self.log_level = log_level

    def get_logger(self, name: str):
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s — %(message)s")

        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.handlers.clear()
        logger.addHandler(handler)
        logger.setLevel(self.log_level)

        return logger
