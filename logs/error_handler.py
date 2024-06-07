from loguru import logger

from .main import LogHandler

"""
    this file all the error related message and logs to a sink
"""

class InfoLogHandler(LogHandler):
    def handle(self, message, level):
        if level == "error":
            logger.error(message)
            
         super().handle(message, level)
