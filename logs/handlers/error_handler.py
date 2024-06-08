from loguru import logger
from logs.base_handle import LogHandler

class ErrorLogHandler(LogHandler):
    def handle(self, message, level):
        if level == "ERROR":
            logger.error(message)
        else:
            super().handle(message, level)
