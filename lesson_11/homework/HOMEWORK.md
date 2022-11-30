## <span style="color:olive">Homework</span>

- You have a very unoptimized method to find prime numbers (below).
- Let's imagine that user passes a huge numbers range - [start=100, end=10_000]
- You have to make this huge range be run in 5 threads
P.S. Think about how would you split this huge range



```python
def get_primes(start: int, end: int) -> list[int]:
    results = []
    for number in range(start, end + 1):
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        if prime:
            results.append(number)
    return results


data = get_primes(10, 20)
print(data)

>>> [11, 13, 17, 19]
```