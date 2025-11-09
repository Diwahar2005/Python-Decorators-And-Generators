from decorators import timer, debug, repeat, Counter
from generators import *


def main():
    print("=" * 50)
    print("🚀 DECORATORS & GENERATORS DEMO")
    print("=" * 50)

    # Demo 1: Decorators
    print("\n" + "🎭 DECORATORS DEMONSTRATION" + "\n" + "-" * 30)

    @timer
    @debug
    def calculate_sum(n):
        """Calculate sum of first n numbers"""
        return sum(range(n + 1))

    @Counter
    def greet(name):
        return f"Hello, {name}!"

    @repeat(num_times=3)
    def say_hello():
        return "Hello World!"

    # Test decorators
    print("Testing @timer and @debug:")
    result1 = calculate_sum(5)
    print(f"Sum result: {result1}\n")

    print("Testing @Counter:")
    greet("Alice")
    greet("Bob")
    greet("Charlie")
    print()

    print("Testing @repeat:")
    results = say_hello()
    print(f"All results: {results}\n")

    # Demo 2: Generators
    print("\n" + "🌀 GENERATORS DEMONSTRATION" + "\n" + "-" * 30)

    print("1. Number Generator (0-4):")
    num_gen = number_generator(5)
    for num in num_gen:
        print(f"   Generated: {num}")

    print("\n2. Fibonacci Generator (first 8 terms):")
    fib_gen = fibonacci_generator(8)
    fib_numbers = list(fib_gen)
    print(f"   Fibonacci: {fib_numbers}")

    print("\n3. Countdown Generator (from 5):")
    countdown = countdown_generator(5)
    for number in countdown:
        print(f"   T-minus: {number}")

    print("\n4. Squares Generator (first 5 squares):")
    squares = squares_generator(5)
    print(f"   Squares: {list(squares)}")

    print("\n5. File Reader Generator:")
    # Create a sample file first
    with open('sample.txt', 'w') as f:
        f.write("Line 1: Hello\nLine 2: World\nLine 3: Python\n")

    file_gen = file_reader_generator('sample.txt')
    for line_num, line_content in file_gen:
        print(f"   Line {line_num}: {line_content}")

    # Demo 3: Combined usage
    print("\n" + "💫 COMBINED USAGE" + "\n" + "-" * 30)

    @timer
    def process_with_generators():
        """Process data using generators"""
        print("   Processing large dataset with generators...")
        data_gen = number_generator(1000000)
        total = sum(data_gen)
        return total

    result = process_with_generators()
    print(f"   Final result: {result}")


if __name__ == "__main__":
    main()