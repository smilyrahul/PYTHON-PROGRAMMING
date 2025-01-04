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

print("Add: ", result1)       
print("Subtract: ", result2)  
print("Multiply: ", result3)  
