# Write a program which accept number from user and print even factors of that number.

iNo = int(input("Enter the number :"))

iCnt = 0

for iCnt in range(2, (iNo//2) + 1, 1):
    if((iNo % iCnt) == 0):
        print(iCnt,end = " ")