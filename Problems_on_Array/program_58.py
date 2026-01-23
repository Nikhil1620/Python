# Accept N numbers from user and return the difference between 
# largest and smallest number.

iNo = int(input("Enter the number of elements :"))

Arr = []

iValue = 0

for i in range(iNo):
    iValue = int(input("Enter the element : "))
    Arr.append(iValue)

iLargest = Arr[0]
iSmallest = Arr[0]

for num in Arr:
    if(iLargest < num):
        iLargest = num

for num in Arr:
    if(iSmallest > num):
        iSmallest = num

iDifference = iLargest - iSmallest

print("The difference between the largest and smallest number is ", iDifference)