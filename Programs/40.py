iNo = int(input("Enter the number : "))
ifactorial1 = 1
ifactorial2 = 1

for i in range(iNo, 0, -1):
    if(i % 2 == 0):
        ifactorial1 = ifactorial1 * i
    else:
        ifactorial2 = ifactorial2 * i

iDifference = ifactorial1 - ifactorial2 

print("The difference is",iDifference)
