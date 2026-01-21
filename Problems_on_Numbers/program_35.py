# Write a program which accept number from user and print its numbers line. 

iNo = int(input("Enter the number : "))

iCnt = 0

for iCnt in range(-iNo, iNo + 1, 1):
    print(iCnt, end = " ")