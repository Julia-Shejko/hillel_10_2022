"""
Using "Operations_with_ROCKYOU.py" you can generate a new file that has only
lines that include requested parameter.
You can see:
    - total lines of this file
    - total size of this file

Before starting work, download the file 📝 "rockyou.txt" to the current folder.
"""

from pathlib import Path
from typing import Generator

from pympler import asizeof

MY_DIR = Path(__file__).parent
ROCKYOU_FILENAME = MY_DIR / "rockyou.txt"
user_input = input("Input the parameter for search: ")


def filter_lines(filename: Path, pattern: str) -> Generator:
    with open(filename, encoding="utf-8") as file:
        while True:
            line = file.readline().replace("\n", "")

            if not line:
                break

            if pattern in line.lower():
                yield line


def count_lines():
    with open(f"{user_input}.txt", encoding="utf-8") as file:
        all_lines = len(file.readlines())
        return all_lines


def file_size():
    size = asizeof.asizeof(MY_DIR / f"{user_input}.txt")
    return size


if __name__ == "__main__":
    with open(f"{user_input}.txt", "w", encoding="utf-8", newline="") as file:
        for my_pattern in filter_lines(ROCKYOU_FILENAME, user_input):
            file.write(my_pattern + "\n")

print(f"✔ The file '{user_input}.txt' created at your request! \n")
print(f"The total number of lines in this file is {count_lines()}\n")
print(f"The total size of file is {file_size()} bytes")
