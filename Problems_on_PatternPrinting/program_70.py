# Accept number of rows and number of columns from user and 
# display below pattern.
# Input : iRow = 4 iCol = 4
# Output : A B C D
#          A B C D
#          A B C D
#          A B C D

iRow = int(input("Enter the number of rows : ")) 
iCol = int(input("Enter the number of coloumns : "))


for i in range(iRow):
    char = 'A'
    for j in range(iCol):
        print(char, end = " ")
        char = chr(ord(char) + 1)
    print()