from PIL import ImageGrab
from dataclasses import dataclass
import pyperclip


@dataclass
class Screenshot:
    left: int
    upper: int
    right: int
    lower: int

    def capture(self):
        screenshot = ImageGrab.grab(bbox=(self.left, self.upper, self.right, self.lower))  # noqa: E501
        screenshot.show()

# Define the bounding box for the screenshot
bounding_box = Screenshot(left=100, upper=100, right=500, lower=500)

# Capture a screenshot of the specified region
bounding_box.capture()

# Copy the screenshot to clipboard
pyperclip.copy(bounding_box)


if __name__ == "__main__":
    screen = Screenshot(left=100, upper=100, right=500, lower=500)