"""
Создайте контекстный менеджер colorizer, который будет печатать
заданным цветом в произвольном блоке кода.
После выхода из блока текст печатается обычным образом
"""

from contextlib import contextmanager

colors = {
    "grey": "\033[90m",
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "pink": "\033[95m",
    "turquoise": "\033[96m",
}


@contextmanager
def colorizer(color):
    if color in colors.keys():
        print(colors[color], end="")
        yield
        print("\033[0m", end="")
    else:
        print(f"{color} not found. Text will be printed in normal font\n")
        yield


with colorizer("red"):
    print("printed in red")
print("printed in default color")
