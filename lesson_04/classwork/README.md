## <span style="color:green">Materials</span>

### Iterator
- Iterator is a design pattern
- for loop write as while with try except

### Generator
- Download the ***[rockyou.txt](https://www.google.com.ua/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjTsaDV2JP4AhWNposKHd00BJYQFnoECAkQAQ&url=https%3A%2F%2Fgithub.com%2Fbrannondorsey%2Fnaive-hashcat%2Freleases%2Fdownload%2Fdata%2Frockyou.txt&usg=AOvVaw3snAERl1mU6Ccr4WFEazBd)*** file

```python
def get_test_file_lines():
    data = []
    with open("text.txt", "r") as file:
        for line in file.readlines():
            data.append(line)
    return data

# Bad one
def generate_test_file_lines():
    with open("text.txt", "r") as file:
        for line in file.readlines():
            yield line

# Good one
def generate_test_file_lines_good():
    with open("text.txt", "r") as file:
        while True:
            line = file.readline().replace("\n", "")
            if not line:
                break
            yield line

for i in get_test_file_lines(): pass
for i in generate_test_file_lines(): pass
for i in generate_test_file_lines_good(): pass
```

Generators
- [Habr](https://habr.com/en/company/domclick/blog/560300/)
- [Programiz](https://www.programiz.com/python-programming/generator)

Debugging
- [IPdb](https://pypi.org/project/ipdb/)
- [Debug in VS Code](https://code.visualstudio.com/docs/editor/debugging)
- [PyCharm debugging](https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html)
