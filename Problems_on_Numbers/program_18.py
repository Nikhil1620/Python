# Write a program which accept number from user and display its multiplication of factors.

iNo = int(input("Enter the number :"))

iCnt = 0
iMulti = 1

for iCnt in range(2, ((iNo // 2) + 1), 1):
    if(iNo % iCnt == 0):
        iMulti = iMulti * iCnt

print("The multiplication of factors of given number is ",iMulti)

