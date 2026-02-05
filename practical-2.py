# Write a python calculator that can perform addition, subtraction, multiplication, and division.

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
result = None
if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y  
elif operation == '*':
    result = x * y
elif operation == '/':
    if y != 0:
        result = x / y
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

print("Result:", result)