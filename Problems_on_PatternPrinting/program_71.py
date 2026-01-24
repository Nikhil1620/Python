# Accept number of rows and number of columns from user and
# display below pattern.
# Input : iRow = 4 iCol = 4
# Output : A B C D
#          a b c d
#          A B C D
#          a b c d

iRow = int(input("Enter the number of rows : ")) 
iCol = int(input("Enter the number of coloumns : "))



for i in range(iRow):
    Char1 = 'A'
    Char2 = 'a'
    for j in range(iCol):
        if(i % 2 == 0):
            print(Char1, end = " ")
            Char1 = chr(ord(Char1) + 1)
        else:
            print(Char2, end = " ")
            Char2 = chr(ord(Char2) + 1)
    print()
