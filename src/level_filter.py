import logging


class LevelFilter(logging.Filter):
    """
    https://stackoverflow.com/a/7447596/190597 (robert)
    """
    level = None

    def __init__(self, level=0):
        self.level = level

    def filter(self, record):
        return record.levelno >= self.level
