# Accept N numbers from user and 
# accept one another number as NO ,return frequency of NO form it. 

iNo = int(input("Enter the number of elements : "))

Arr = []

iValue = 0

for i in range(iNo):
    iValue = int(input("Enter the element : "))
    Arr.append(iValue)

iNum = int(input("Enter the number : "))

iFrequency = 0

for num in Arr:
    if(num == iNum):
        iFrequency = iFrequency + 1

print("The frequency of given number is ", iFrequency)
