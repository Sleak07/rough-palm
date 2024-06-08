"""
    this file contains the specific way in which the log should be format
    
"""
import sys
from loguru import logger

def format_log():
    logger.remove(0)
    logger.add(sys.stdout,format="{format} {level} {time}",level="DEBUG")
