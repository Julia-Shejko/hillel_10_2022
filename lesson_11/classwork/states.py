import random
from dataclasses import dataclass, field
from enum import Enum, auto


def random_delay():
    return random.random() * 3


def random_countdown():
    return random.randint(1, 5)


class Status(Enum):
    NOT_STARTED = auto()
    STARTED = auto()
    FINISHED = auto()


class Operations(Enum):
    WAIT = auto()
    STOP = auto()


@dataclass
class Rocket:
    status: Status = Status.NOT_STARTED
    delay: float = field(default_factory=random_delay)
    countdown: int = field(default_factory=random_countdown)

    def step(self):
        if self.status is Status.NOT_STARTED:
            self.status = Status.STARTED
            return Operations.WAIT, self.delay
        if self.status is Status.STARTED:
            if self.countdown == 0:
                self.status = Status.FINISHED
            else:
                self.countdown -= 1
                return Operations.WAIT, 1
        if self.status is Status.FINISHED:
            return Operations.STOP, None


def main():
    print("Hello")


# run_sync()


if __name__ == "__main__":
    main()
