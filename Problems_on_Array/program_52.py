# Accept N numbers from user and accept one another 
# number as NO ,return index of first occurrence of that NO. 

iNo = int(input("Enter the number of elements : "))

Arr = []

iValue = 0

for i in range(iNo):
    iValue = int(input("Enter the element : "))
    Arr.append(iValue)

iNum = int(input("Enter the number : "))

iCnt = 0
Bfound = False

for num in Arr:
    if(num == iNum):
        print("The index of the given number is ",iCnt)
        Bfound = True
        break
    iCnt = iCnt + 1

if(Bfound == False):
    print("The Array does not conatin the given element.")