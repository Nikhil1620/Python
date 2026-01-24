# Accept number of rows and number of columns from user and display
# below pattern.
# Input : iRow = 4 iCol = 3
# Output : * * *
#          * * *
#          * * *
#          * * * 

iRows = int(input("Enter the number of rows : ")) 
iCol = int(input("Enter the number of coloumns : "))

for i in range(iRows):
    for j in range(iCol):
        print("*", end = " ")
    print()

