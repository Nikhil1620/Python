# Accept number of rows and number of columns from user and 
# display below pattern.
# Input : iRow = 3 iCol = 4
# Output : 1 1 1 1
#          2 2 2 2
#          3 3 3 3

iRow = int(input("Enter the number of rows : ")) 
iCol = int(input("Enter the number of coloumns : "))

for i in range(1, iRow + 1, 1):
    for j in range(iCol):
        print(i, end = " ")
    print()