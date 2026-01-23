# Accept N numbers from user and return difference between 
# frequency of even number and odd numbers.

iNo = int(input("Enter the number of elements : "))

Arr = []

iValue = 0

for i in range(iNo):
    iValue = int(input("Enter the elements : "))
    Arr.append(iValue)

iEvenFrequency = 0
iOddFrequency = 0

for num in Arr:
    if(num % 2 == 0):
        iEvenFrequency = iEvenFrequency + 1
    else:
        iOddFrequency = iOddFrequency + 1

iDifference = iEvenFrequency - iOddFrequency

if(iDifference < 0):
    iDifference = -iDifference

print("The Difference is ", iDifference)