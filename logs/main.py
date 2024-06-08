from logs.handlers.debug_handler import DebugLogHandler
from logs.handlers.info_handler import InfoLogHandler
from logs.handlers.warning_handler import WarningLogHandler
from logs.handlers.error_handler import ErrorLogHandler
from logs.rotating_log import RotatingFileLogHandler
from logs.format_log import format_log

def setup_logging_chain():
    format_log()
    
    rotating_file_handler = RotatingFileLogHandler("app.log", rotation="1 MB")
    error_handler = ErrorLogHandler(next_handler=rotating_file_handler)
    warning_handler = WarningLogHandler(next_handler=error_handler)
    info_handler = InfoLogHandler(next_handler=warning_handler)
    debug_handler = DebugLogHandler(next_handler=info_handler)
    
    return debug_handler

def log_message(message, level):
    handler_chain = setup_logging_chain()
    handler_chain.handle(message, level)

# Example usage
if __name__ == "__main__":
    log_message("This is a debug message", "DEBUG")
    log_message("This is an info message", "INFO")
    log_message("This is a warning message", "WARNING")
    log_message("This is an error message", "ERROR")
