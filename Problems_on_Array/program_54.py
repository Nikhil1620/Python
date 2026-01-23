# Accept N numbers from user and accept Range, 
# Display all elements from that range 

iNo = int(input("Enter the number of elements : "))

Arr = []

iValue = 0

for i in range(iNo):
    iValue = int(input("Enter the element : "))
    Arr.append(iValue)

iFirst = int(input("Enter the first end : "))
iSecond = int(input("Enter the last end : "))

for num in Arr:
    if(num > iFirst and num < iSecond):
        print(num, end = " ")