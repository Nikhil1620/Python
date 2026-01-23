# Accept N numbers from user and accept one another 
# number as NO ,return index of last occurrence of that NO.

iNo = int(input("Enter the number of elements : "))

Arr = []

iValue = 0

for i in range(iNo):
    iValue = int(input("Enter the element : "))
    Arr.append(iValue)

iNum = int(input("Enter the number : "))

iIndex = -1

for i in range(len(Arr)):
    if(Arr[i] == iNum):
        iIndex = i


if(iIndex != -1):
    print("The index of the last occured element is ",iIndex)
else:
    print("The given element is not in the array")
