from loguru import logger

from .main import LogHandler

"""
    this file all the debug related message and logs to a sink
"""

class InfoLogHandler(LogHandler):
    def handle(self, message, level):
        if level == "debug":
            logger.debug(message)
            
        super().handle(message, level)
