# Write a program which accept one number from user and print that number of even numbers on screen.

iNo = int(input("Enter the number of frequency :"))

iCnt = 0

for iCnt in range(1, (iNo*2), 1):
    if(iCnt % 2 == 0):
        print(iCnt, end = " ")
    