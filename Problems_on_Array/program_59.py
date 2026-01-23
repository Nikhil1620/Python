# Accept N numbers from user and display all such 
# numbers which contains 3 digits in it.

iNo = int(input("Enter the number of elements :"))

Arr = []

iValue = 0

for i in range(iNo):
    iValue = int(input("Enter the element : "))
    Arr.append(iValue)

print("3-digit numbers are:")

for num in Arr:
    temp = abs(num)  
    iDigitCount = 0

    if temp == 0:
        iDigitCount = 1
    else:
        while temp != 0:
            iDigitCount += 1
            temp = temp // 10

    if iDigitCount == 3:
        print(num)