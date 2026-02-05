# Write a program to find factorial of a number using for loop

num = int(input("Enter a number to find its factorial: "))
factorial = 1
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(2, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")