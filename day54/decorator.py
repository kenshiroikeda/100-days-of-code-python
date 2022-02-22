import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(fun):
    def wrapper_function():
        start_time = time.time()
        fun()
        end_time = time.time()
        spent_time = end_time - start_time
        print(f"spent_time : {spent_time}")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
