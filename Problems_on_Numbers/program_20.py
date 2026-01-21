# Write a program which accept number from user and display all its non factors. 

iNo = int(input("Enter the number : "))

iCnt = 0

for iCnt in range(1, (iNo + 1), 1):
    if(iNo % iCnt != 0):
        print(iCnt, end = " ")