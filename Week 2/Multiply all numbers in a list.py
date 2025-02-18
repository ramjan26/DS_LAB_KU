def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)
print(is_perfect(28))  # Output: True (28 is a perfect number)