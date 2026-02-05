# WAP to check vowel or consonant

char = input("Enter a single alphabet character: ")

if char in 'aeiouAEIOU':
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")
