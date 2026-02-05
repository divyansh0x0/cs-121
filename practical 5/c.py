# WAP to find a number is prime or not
num = int(input("Enter an integer:"))
for i in range(2, num//2):
    if num % i == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")
