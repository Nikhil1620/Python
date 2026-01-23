# Accept N numbers from user and return frequency of even numbers.

iNo = int(input("Enter the number of elements : "))

Arr = []

iValue = 0

for i in range(iNo):
    iValue = int(input("Enter the elements : "))
    Arr.append(iValue)

iFrequency = 0

for num in Arr:
    if(num % 2 == 0):
        iFrequency = iFrequency + 1

print("The Frequency of even number in the given array is ", iFrequency)
