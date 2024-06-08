from loguru import logger
from logs.base_handle import LogHandler

class WarningLogHandler(LogHandler):
    def handle(self, message, level):
        if level == "WARNING":
            logger.warning(message)
        else:
            super().handle(message, level)
