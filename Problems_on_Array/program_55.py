# Accept N numbers from user 
# and return product of all odd elements. 

iNo = int(input("Enter the number of elements :"))

Arr = []

iValue = 0

for i in range(iNo):
    iValue = int(input("Enter the element : "))
    Arr.append(iValue)

iProduct = 1

for num in Arr:
    if(num % 2 != 0):
        iProduct = iProduct * num

print("The product of all the odd elements in the given array is ", iProduct)