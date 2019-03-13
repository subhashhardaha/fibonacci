def fibonacci_nth_recursive(n):
    if n < 0:
        return None
    # First Fibonacci number is 0
    elif n == 0:
        return 0
    # Second Fibonacci number is 1
    elif n == 1:
        return 1
    else:
        return fibonacci_nth(n - 1) + fibonacci_nth(n - 2)


def fibonacci_nth(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
