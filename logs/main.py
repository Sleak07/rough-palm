"""
This main.py file defines the abstract class which serves the base for logging 
"""      
from abc import ABC,abstractmethod

class LogHandler(ABC):
    def __init__(self) -> None:
        self ._next_handler = None

    # this method transfer the logging request to next handler based on level
    def set_next(self,handler):
        self._next_handler = handler
        return handler
    
    # the next method handles the log level
    @abstractmethod
    def handle(self, message, level):
        if self._next_handler:
            self._next_handler.handle(message, level) 
        

    
        
