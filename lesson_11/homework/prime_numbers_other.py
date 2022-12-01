"""
Let's imagine that user passes a huge numbers range - from 100 to 10_000.
This huge range will be run in 5 threads.

You can change these values in the corresponding variables (start, end, amount)
"""

from threading import Thread

result = []


def group_numbers(start: int, end: int, amount: int) -> list:
    numbers = [_ for _ in range(start, end + 1)]
    numbers1 = []
    start_index = 0
    for i in range(1, amount + 1):
        numbers1.append(numbers[start_index::amount])
        start_index += 1
    return numbers1


def get_primes(num: list) -> list:
    for i in num:
        counter = 0
        for j in range(1, i):
            if i % j == 0:
                counter += 1
        if counter == 1:
            result.append(i)
    return result


def run_threads(formed_list: list) -> list:
    index_indicator = 0
    for _ in formed_list:
        thread = Thread(target=get_primes, args=[formed_list[index_indicator]])
        thread.start()
        index_indicator += 1
    return result


def main():
    start = 100
    end = 10000
    amount = 5
    grouped_numbers = group_numbers(start, end, amount)
    final_result = run_threads(grouped_numbers)
    return sorted(final_result)


if __name__ == "__main__":
    data = main()
    print(data)
