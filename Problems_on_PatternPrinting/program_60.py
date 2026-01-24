# 1. Accept number from user and display below pattern.
# Input : 5
# Output : A B C D E 

iNo = int(input("Enter the number : "))
char = 'A'

for i in range(iNo):
    print(char,end =" ")
    char = chr(ord(char) + 1)

