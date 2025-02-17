x = 100
def calculate_something(a, b):
    """This function has multiple code quality issues"""
    # Unused variable
    unused_var = 42
    # Nested if statements that are too complex
    if a > 0:
        if b > 0:
            if a > b:
                if a - b > 10:
                    return a * b
                else:
                    return a + b
            else:
                return b - a
        else:
            return None
    else:
        return None
# Function with too many parameters
def process_data(param1, param2, param3, param4, param5, param6, param7, param8):
    # Empty except block - bad practice
    try:
        result = param1 + param2 + param3 + param4
        return result / (param5 + param6 + param7 + param8)
    except:
        pass
# Duplicate code block
def first_function():
    print("Starting process")
    for i in range(10):
        print(f"Processing item {i}")
        if i % 2 == 0:
            print("Even number found")
    print("Ending process")
# Duplicate code block
def second_function():
    print("Starting process")
    for i in range(10):
        print(f"Processing item {i}")
        if i % 2 == 0:
            print("Even number found")
    print("Ending process")
if __name__ == "__main__":
    # Magic number used directly
    result = calculate_something(15, 27)
    # Unused import
    import json
    # Hard-coded credentials (security issue)
    password = "admin123"
