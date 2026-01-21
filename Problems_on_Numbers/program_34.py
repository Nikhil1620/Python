# Write a program which accept number from user and print numbers 
# till that number.

iNo = int(input("Enter the number : "))

iCnt = 0

for iCnt in range(1, iNo+1, 1):
    print(iCnt, end = " ")