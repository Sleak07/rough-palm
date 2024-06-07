from loguru import logger

from .main import LogHandler

"""
    this file all the info related message and logs to a sink
"""

class InfoLogHandler(LogHandler):
    def handle(self, message, level):
        if level == "info":
            logger.info(message)
            
         super().handle(message, level)
    
