def my_decorator(func):
    def wrapper(name):  # wrapper принимает name
        print("До вызова")
        func(name)       # func тоже получает name
        print("После вызова")
    return wrapper

@my_decorator
def greet(name):
    print(f"Пока, {name}!")
    