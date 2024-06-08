from loguru import logger
from logs.base_handle import LogHandler

class DebugLogHandler(LogHandler):
    def handle(self, message, level):
        if level == "DEBUG":
            logger.debug(message)
        else:
            super().handle(message, level)
