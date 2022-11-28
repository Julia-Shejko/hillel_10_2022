def random_numbers():
    for i in range(10):
        yield i


def random_numbers2():
    for i in range(10):
        yield i


def bar():
    yield from random_numbers()
    yield from random_numbers2()


# num_1 = foo()
# print(num_1)


var = bar()
print(var)
print(next(var))
print(next(var))
print(next(var))
