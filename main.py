import pyperclip
from typing import  Union

def copy_to_clipboard(user_input: Union[str, int]) -> None:
    pyperclip.copy(str(user_input))
    print("Copied to clipboard")


if __name__ == "__main__":
    user_input = input("Enter your text or number: ")
    copy_to_clipboard(user_input)
    