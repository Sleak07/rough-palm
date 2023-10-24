import pyperclip
from typing import Union
import time
from dataclasses import dataclass


@dataclass
class Clipboard:
    text: str
    num: int
    user_input: Union[str, int, bytes]      
    time: float = 0.0

# Copies the content the user provides to clipboard

    def copy_to_clipboard(
        self,
        user_input: Union[
            str,
            int,
            bytes,
        ],
    ) -> None:
        pyperclip.copy(str(user_input))

# Checks whether the user has given the specified input or raise error

    def waiting_time(self, user_input: Union[str, int]) -> None:
        init = time.time()
        self.copy_to_clipboard(user_input)
        elapsed_time = time.time() - init
        print("Copied to clipboard")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")

        if time.time() - init > 5:
            print("Time is up")
        else:
            pass


# Calls the main function to execute the code
if __name__ == "__main__":
    user_input = input("Enter your text or number : ")
    clipboard = Clipboard(text="example", num=1, user_input=user_input)
    clipboard.waiting_time(user_input)
