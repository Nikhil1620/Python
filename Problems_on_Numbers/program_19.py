# Write a program which accept number from user and display its factors in decreasing order. 

iNo = int(input("Enter the number : "))

iCnt = 0

for iCnt in range(iNo // 2, 0, -1):
    if(iNo % iCnt == 0):
        print(iCnt, end = " ")

    