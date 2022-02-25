# Create the logging_decorator() function 👇
def logging_decorator(fn):
    def wrapper(*args):
        print(f"function name is {fn.__name__}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(1, 2, 3)
