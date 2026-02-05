# Write a program to find fibonacci series up to n terms using for loop

n = int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1

for i in range(0,n):
    print(a)
    temp = b
    b += a
    a = temp
