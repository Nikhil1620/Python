# Accept number of rows and number of columns from user and 
# display below pattern.
# Input : iRow = 3 iCol = 5
# Output : 5 4 3 2 1
#          5 4 3 2 1
#          5 4 3 2 1

iRow = int(input("Enter the number of rows : ")) 
iCol = int(input("Enter the number of coloumns : "))

for i in range(1, iRow + 1, 1):
    for j in range(iCol, 0, -1):
        print(j, end = " ")
    print()