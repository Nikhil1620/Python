# Accept number of rows and number of columns from user and 
# display below pattern.
# Input : iRow = 3 iCol = 5
# Output : A A A A A
#          B B B B B
#          C C C C C

iRow = int(input("Enter the number of rows : ")) 
iCol = int(input("Enter the number of coloumns : "))

char = 'A'

for i in range(iRow):
    for j in range(iCol):
        print(char, end = " ")
    char = chr(ord(char) + 1)
    print()