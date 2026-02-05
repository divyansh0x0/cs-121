# write a python program to swap two values without using third variable

a = input("Enter first value: ")
b = input("Enter second value: ")

print("Before swapping: a =", a, ", b =", b)

a, b = b, a

print("After swapping: a =", a, ", b =", b)