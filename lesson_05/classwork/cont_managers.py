from contextlib import contextmanager

# file = open('some_file.txt', 'w', encoding='utf-8')
# file.write('Hello')
# file.close()

# print(dir(file))


# for item in range(10000000):
#     file = open('some_file.txt', 'w', encoding='utf-8')
#     file.write('Hello')


# print("end")


# with open('some_file.txt', 'w', encoding='utf-8') as file:
#     file.write('Hello')


# class File:
#     def __init__(self, file, method):
#         self.file_obj = open(file, method)
#
#     def __enter__(self):
#         return self.file_obj
#
#     def __exit__(self, type, value, traceback):
#         self.file_obj.close()


# # with File('some_file.txt', 'w') as file:
# #     file.write("file")


@contextmanager
def some_file(file_name, method):
    func = open(file_name, method)

    try:
        yield func

    finally:
        func.close()


with some_file("some_file.txt", "w") as file:
    file.write("file")


# print('\033[93m', end='')
# print('aaa')
# print('bbb')
# print('\033[0m', end='')
# print('ccc')
