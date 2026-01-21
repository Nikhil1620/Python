# Write a program which accept number from user and return difference between
# summation of all its factors and non factors.

iNo = int(input("Enter the number : "))

iCnt = 0

iAddition1 = 0
iAddition2 = 0

iDifference = 0

for iCnt in range(1, (iNo+1), 1):
    if(iNo % iCnt == 0):
        iAddition1 = iAddition1 + iCnt
    else:
        iAddition2 = iAddition2 + iCnt

print(iAddition1)
print(iAddition2)

iDifference = iAddition1 - iAddition2

if(iDifference < 0):
    iDifference = -(iDifference)

print("The difference between the factors and non factors of the given numbee is ", iDifference)