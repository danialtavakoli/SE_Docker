"""Basic arithmetic helpers used to demonstrate a Python CI/CD pipeline."""


def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def subtract(a, b):
    return a - b


if __name__ == "__main__":
    print(multiply(2, 3))   # 6
    print(add(2, 3))        # 5
    print(divide(10, 2))    # 5.0
    print(subtract(10, 2))  # 8
