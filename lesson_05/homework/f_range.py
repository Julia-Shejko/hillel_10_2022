"""
В Питоне нет класса frange, который бы работал с float.
Создать свою версию такого класса, который бы поддерживал
интерфейс стандартного range, но работал при этом с float.
"""


class frange:
    def __init__(self, left, right=None, step=1):
        self._left = left
        self._right = right
        self._step = step

        if self._right is None:
            self._left, self._right = 0, self._left

    def __next__(self):

        if self._step > 0:
            if self._left < self._right:
                result = self._left
                self._left += self._step
                return result
            else:
                raise StopIteration("stop")
        else:
            if self._left > self._right:
                result = self._left
                self._left += self._step
                return result
            else:
                raise StopIteration("stop")

    def __iter__(self):
        return self


assert list(frange(5)) == [0, 1, 2, 3, 4]
assert list(frange(2, 5)) == [2, 3, 4]
assert list(frange(2, 10, 2)) == [2, 4, 6, 8]
assert list(frange(10, 2, -2)) == [10, 8, 6, 4]
assert list(frange(2, 5.5, 1.5)) == [2, 3.5, 5]
assert list(frange(1, 5)) == [1, 2, 3, 4]
assert list(frange(0, 5)) == [0, 1, 2, 3, 4]
assert list(frange(0, 0)) == []
assert list(frange(100, 0)) == []

print("SUCCESS!")
