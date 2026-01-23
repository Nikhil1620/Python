# Accept N numbers from user and return the largest number

iNo = int(input("Enter the number of elements :"))

Arr = []

iValue = 0

for i in range(iNo):
    iValue = int(input("Enter the element : "))
    Arr.append(iValue)

iLargest = Arr[0]

for num in Arr:
    if(iLargest < num):
        iLargest = num

print("The largest numner in the given array is ", iLargest)