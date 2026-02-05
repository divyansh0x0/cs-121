# WAP to print the following star pattern
# * 
# * * 
# * * *
# * * * *

n = int(input("Enter number of lines: "))
i = 1

while i <= n:
    print("*  "* i)
    i+=1