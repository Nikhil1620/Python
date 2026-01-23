# Accept N numbers from user and return the largest number

iNo = int(input("Enter the number of elements : "))

Arr = []

iValue = 0

for i in range(iNo):
    iValue = int(input("Enter the element : "))
    Arr.append(iValue)

LargestNum = Arr[0]
for num in Arr:
    if(num > LargestNum):
        LargestNum = num

print("The Largest Number is ",LargestNum)


