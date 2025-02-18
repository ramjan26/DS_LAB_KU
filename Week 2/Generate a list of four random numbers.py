import random

def generate_random_numbers():
    return [random.randint(1, 100) for _ in range(4)]
print(generate_random_numbers())  # Output: [random numbers]
