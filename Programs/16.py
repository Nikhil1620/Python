iNo = int(input("Enter the number : "))
iAddition = 0

for i in range(1,iNo+1, 1):
    if(iNo % i != 0):
        iAddition = iAddition + i

print("The Addition is",iAddition)