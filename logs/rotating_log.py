from loguru import logger
from logs.base_handle import LogHandler

class RotatingFileLogHandler(LogHandler):
    def __init__(self, file_path, rotation, next_handler=None):
        super().__init__(next_handler)
        self.file_path = file_path
        logger.add(self.file_path, rotation=rotation, level="INFO")

    def handle(self, message, level):
        if level in ["DEBUG", "INFO", "WARNING", "ERROR"]:
            logger.log(level, message)
        else:
            super().handle(message, level)
