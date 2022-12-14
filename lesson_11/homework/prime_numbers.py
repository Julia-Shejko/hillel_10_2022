"""
Let's imagine that user passes a huge numbers range - from 100 to 10_000.
This huge range will be run in 5 threads.

You can change these values in the corresponding variables (start, end, amount)
"""

from threading import Thread

result = []


def group_numbers(start: int, end: int) -> list:
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
    len_list = len(formed_list)
    parts_number = len_list // threads_number
    start_index = 0
    end_index = start_index + parts_number

    for i in range(threads_number):
        if len_list <= threads_number:
            thread = Thread(target=get_primes, args=[formed_list[start_index:len_list]])
            thread.start()
            break
        elif end_index + parts_number <= len_list - 1:
            thread = Thread(target=get_primes, args=[formed_list[start_index:end_index]])
            thread.start()
            start_index += parts_number
            end_index += parts_number
        else:
            thread = Thread(target=get_primes, args=[formed_list[start_index:len_list]])
            thread.start()
    return result


def main():
    start = 100
    end = 10000
    amount = 5
    grouped_numbers = group_numbers(start, end)
    final_result = run_threads(grouped_numbers, amount)
    return sorted(final_result)


if __name__ == "__main__":
    data = main()
    print(data)
