#Write a generator function to generate the Fibonacci series
def fibonacci_list(n):
    """Return a list containing the first n numbers in the Fibonacci series."""
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
# Function to print the Fibonacci series with additional formatting
def print_fibonacci(series):
    print("Fibonacci Series:")
    for index, value in enumerate(series, start=1):
        print(f"Term {index}: {value}")
# User input to define the length of the Fibonacci sequence
total_numbers = int(input("Enter the number of Fibonacci terms to generate: "))
# Generating and displaying the Fibonacci series
fib_sequence = fibonacci_list(total_numbers)
print_fibonacci(fib_sequence)
