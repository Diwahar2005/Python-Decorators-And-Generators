def number_generator(limit):
    """Simple generator that yields numbers up to limit"""
    num = 0
    while num < limit:
        yield num
        num += 1

def fibonacci_generator(n):
    """Generator that yields Fibonacci sequence up to n terms"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def file_reader_generator(filename):
    """Generator that reads file line by line"""
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                yield line_number, line.strip()
    except FileNotFoundError:
        yield f"❌ File {filename} not found!"

def countdown_generator(start):
    """Generator that counts down from start to 0"""
    while start >= 0:
        yield start
        start -= 1

# Generator expression example
def squares_generator(n):
    """Generator expression for squares"""
    return (x**2 for x in range(n))