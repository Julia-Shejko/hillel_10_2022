from typing import Callable


def greeting():
    print("Hello")


another_greeting = greeting


def another(something: Callable) -> None:
    something()


another(greeting)
