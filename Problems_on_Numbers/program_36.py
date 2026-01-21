# Write a program which accepts N from user and 
# print all odd numbers up to N.

iNo = int(input("Enter the number : "))

iCnt = 0

for iCnt in range(1, iNo+1, 1):
    if(iCnt % 2 != 0):
        print(iCnt,end = " ")