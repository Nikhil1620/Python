iNo = int(input("Enter the number : "))

iAdd1 = 0
iAdd2 = 0

for i in range(1, iNo+1, +1):
    if(iNo % i == 0):
        iAdd1 = iAdd1 + i
    else:
        iAdd2 = iAdd2 + i

iDifference = iAdd1 - iAdd2

print("the difference between summation of all its factors and non factors is", iDifference)