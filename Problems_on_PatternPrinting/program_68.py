# Accept number of rows and number of columns from user and 
# display below pattern.
# Input : iRow = 3 iCol = 4
# Output : * # * #
#          * # * #
#          * # * #

iRow = int(input("Enter the number of rows : ")) 
iCol = int(input("Enter the number of coloumns : "))

for i in range(iRow):
    for j in range(iCol):
        if(j % 2 == 0):
            print("*",end = " ")
        else:
            print("#",end = " ")
    print()