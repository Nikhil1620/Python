# Accept N numbers from user and return the smallest number.

iNo = int(input("Enter the number of elements :"))

Arr = []

iValue = 0

for i in range(iNo):
    iValue = int(input("Enter the element : "))
    Arr.append(iValue)

iSmallest = Arr[0]

for num in Arr:
    if(iSmallest > num):
        iSmallest = num

print("The smallest numner in the given array is ", iSmallest)