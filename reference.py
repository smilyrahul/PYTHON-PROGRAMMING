# Example of passing a function by reference

# Define some functions to pass
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def calculate(operation, a, b):
    return operation(a, b)


result1 = calculate(add, 10, 5)        
result2 = calculate(subtract, 10, 5)   
result3 = calculate(multiply, 10, 5)   

print("Add: ", result1)       # Output: 15
print("Subtract: ", result2)  # Output: 5
print("Multiply: ", result3)  # Output: 50
