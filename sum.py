"""
sum.py
Simple script to compute the sum of two numbers entered by the user.
"""

def sum_two_numbers(a, b):
    """Return the sum of a and b."""
    return a + b


if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Sum:", sum_two_numbers(a, b))
    except ValueError:
        print("Please enter valid numbers.")
