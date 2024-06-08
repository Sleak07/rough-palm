from loguru import logger
from logs.base_handle import LogHandler

class InfoLogHandler(LogHandler):
    def handle(self, message, level):
        if level == "INFO":
            logger.info(message)
        else:
            super().handle(message, level)
