"""
Let's imagine that user passes a huge numbers range - from 100 to 10_000.
This huge range will be run in 5 threads.

You can change these values in the corresponding variables (start, end, amount)
"""

from threading import Thread

result = []


def group_numbers(start: int, end: int, amount: int) -> list:
    numbers = [_ for _ in range(start, end + 1)]
    return numbers


def get_primes(num: list) -> list:
    for i in num:
        counter = 0
        for j in range(1, i):
            if i % j == 0:
                counter += 1
        if counter == 1:
            result.append(i)
    return result


def run_threads(formed_list: list, threads_number) -> list:
    parts_number = len(formed_list) // threads_number
    start_index = 0
    end_index = start_index + parts_number

    for _ in formed_list:
        if start_index <= len(formed_list) - 1:
            thread = Thread(target=get_primes, args=[formed_list[start_index:end_index]])
            thread.start()
            start_index += parts_number
            end_index += parts_number
    return result


def main():
    start = 1
    end = 100
    amount = 5
    grouped_numbers = group_numbers(start, end, amount)
    final_result = run_threads(grouped_numbers, amount)
    return sorted(final_result)


if __name__ == "__main__":
    data = main()
    print(data)
