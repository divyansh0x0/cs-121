# Python program to demonstrate type conversion from float to int and string to int

float_num = float(input("Enter a float number: "))
str_num = input("Enter a string number: ") 

print("Type of float_num:", type(float_num))
print("Type of str_num:", type(str_num))
int_from_float = int(float_num)
int_from_str = int(str_num) 

print("Integer from float:", int_from_float)
print("Integer from string:", int_from_str)

print("Type of int_from_float:", type(int_from_float))
print("Type of int_from_str:", type(int_from_str))