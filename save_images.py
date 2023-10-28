"""Taking a screeenshot of image and saving it to clipboard"""

from PIL import ImageGrab
import pyperclip
import io
from dataclasses import dataclass


@dataclass
class Screenshot:
    def __init__(self, image):
        self.image = image


""" Takes  a screenshot by user"""


def take_screenshot():
    screen_snap = ImageGrab.grab()

    # save screensnap as bytesobject
    buffer = io.BytesIO()
    screen_snap.save(buffer, format="PNG")

    screen_bytes = buffer.getvalue()

    # save bytes to clipboard
    pyperclip.copy(screen_bytes)


if __name__ == "__main__":
    take_screenshot()
