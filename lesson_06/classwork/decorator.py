def logger():
    def super_wrapper(char: str):
        print("BLABLABLA")

        def wrapper(func):
            def inner():
                print(char * 10)
                func()
                print(char * 10)

            return inner

        return wrapper

    return super_wrapper


@logger()(char="*")
def greeting_john():
    print("Hello John!")


@logger()(char="#")
def greeting_marry():
    print("Hello Marry!")


# logger(greeting_john)
# logger(greeting_marry)
greeting_john()
greeting_marry()
