# Accept one character from user and convert case of that character. 

ch = input("Enter the character : ")

if ch.islower():
    print(ch.upper())
elif ch.isupper():
    print(ch.lower())
else:
    print("Enter the valid character")