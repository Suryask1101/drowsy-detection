import os  # Unused import (SonarQube will flag it)
import random  # Unused import (SonarQube will flag it)
# Function with code duplication (SonarQube will flag this as code duplication)
def calculate_sum(a, b):
    result = a + b
    print(f"Sum: {result}")
    return result
def calculate_total(x, y):
    total = x + y
    print(f"Total: {total}")
    return total
# Complex function with multiple nested conditions
def complex_function(a, b, c):
    if a > 10:
        if b < 5:
            if c == 3:
                return a + b + c
            elif c == 5:
                return a - b + c
            else:
                return a * b - c
        else:
            return a / (b + 1) * c
    else:
        return a + b - c
# Hardcoded values (magic numbers, SonarQube will flag it)
def process_data():
    value = 10  # Hardcoded value, should be defined as a constant or passed as a parameter
    if value > 5:
        return value * 2
    else:
        return value + 3
# Another example of code duplication
def compute_area(length, width):
    area = length * width
    print(f"Area: {area}")
    return area
def calculate_rectangle_area(length, width):
    area = length * width  # Same as compute_area, SonarQube will flag it as duplicated code
    print(f"Rectangle Area: {area}")
    return area
# Nested functions with high complexity
def nested_function_example(a, b):
    if a > 0:
        if b > 0:
            return a + b
        elif b == 0:
            return a
        else:
            return a - b
    else:
        return 0
# Code with hardcoded strings
def print_message():
    print("Hello, World!")  # Hardcoded string (should be parameterized or defined in a constant)
# Testing multiple functions together
def main():
    calculate_sum(5, 10)
    calculate_total(3, 7)
    result = complex_function(15, 3, 5)
    print(f"Result of complex function: {result}")
    result = process_data()
    print(f"Processed data result: {result}")
    compute_area(4, 5)
    calculate_rectangle_area(4, 5)
    nested_function_example(1, 2)
    print_message()
if __name__ == "__main__":
    main()


Message Akhil TP









