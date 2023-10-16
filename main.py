import time
from typing import Union

import pyperclip


def copy_to_clipboard(user_input: Union[str, int]) -> None:
    pyperclip.copy(str(user_input))


def waiting_time(user_input: Union[str, int]) -> None:
    init = time.time()
    copy_to_clipboard(user_input)
    elapsed_time = time.time() - init
    print("Copied to clipboard")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

    if time.time() - init > 5:
        print("Time is up")
    else:
        pass

if __name__ == "__main__":
    user_input = input("Enter your text or number: ")
    copy_to_clipboard(user_input)
    waiting_time(user_input)
    
