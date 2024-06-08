from abc import ABC

"""
    this file defines the basis for handling log ,
    1st function sets next handler
    2nd and 3rd function correspond to passing to next one and hence logging the message to sink
"""

class LogHandler(ABC):
    def __init__(self,next_handler) -> None:
        self._next_handler = next_handler


   def handle(self, message, level):
        if self.next_handler:
            self.next_handler.handle(message, level)
