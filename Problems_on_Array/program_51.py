# Accept N numbers from user and accept one another
# number as NO ,check whether NO is present or not.

iNo = int(input("Enter the number of elements : "))

Arr = []

iValue = 0

for i in range(iNo):
    iValue = int(input("Enter the element : "))
    Arr.append(iValue)

iNum = int(input("Enter the number : "))

Bfound = False

for num in Arr:
    if(num == iNum):
        Bfound = True
        break

if(Bfound == True):
    print("The Array contains given number.")
else:
    print("The Array does not contain given number.")