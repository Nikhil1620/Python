# Write a program which accept N and print first 5 multiples of N. 

iNo = int(input("Enter the number : "))

iCnt = 0

for iCnt in range(1, (iNo*5) + 1, 1):
    if(iCnt % iNo == 0):
        print(iCnt,end = " ")