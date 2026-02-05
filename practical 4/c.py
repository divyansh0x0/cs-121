# Write a simple calculator using if elif else statement

print("Simple Calculator")

choice = input("Enter operation (+, -, *, /, %): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = None
if choice == '+':
    result = num1 + num2
elif choice == '-':
    result = num1 - num2
elif choice == '*': 
    result = num1 * num2
elif choice == '/':
    result = num1 / num2
elif choice == '%':
    result = num1 % num2
else:
    print("Invalid operation selected.")


print(f"{num1} {choice} {num2} = {result}")