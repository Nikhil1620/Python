# Write a program which accept number from user and return summation of all its non factors.

iNo = int(input("Enter the number : "))

iCnt = 0

iAddition = 0

for iCnt in range(1, iNo + 1, 1):
    if(iNo % iCnt != 0):
        iAddition = iAddition + iCnt

print("The summation of non factors of the given number is ", iAddition)