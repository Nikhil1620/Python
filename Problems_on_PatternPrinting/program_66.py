# Accept number of rows and number of columns from user and
#display below pattern.
# Input : iRow = 4 iCol = 3
# Output : 1 2 3
#          1 2 3
#          1 2 3
#          1 2 3

iRows = int(input("Enter the number of rows : ")) 
iCol = int(input("Enter the number of coloumns : "))


for i in range(1, iRows + 1, 1):
    for j in range(1, iCol + 1, 1):
        print(j,end = " ")
        j = j + 1
    print()

