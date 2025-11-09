import time
from functools import wraps


def timer(func):
    """Decorator that measures function execution time"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"⏰ {func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result

    return wrapper


def debug(func):
    """Decorator that prints function details"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🔍 Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"✅ {func.__name__} returned: {result}")
        return result

    return wrapper


def repeat(num_times=2):
    """Decorator that repeats function execution"""

    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(num_times):
                print(f"🔄 Repeat #{i + 1} of {func.__name__}")
                result = func(*args, **kwargs)
                results.append(result)
            return results

        return wrapper

    return decorator_repeat


# Class-based decorator
class Counter:
    """Decorator that counts function calls"""

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"🎯 {self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)