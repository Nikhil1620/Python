# Find Largest Among Three Numbers 

iNo1 = int(input("Enter the first number : "))
iNo2 = int(input("Enter the second number : "))
iNo3 = int(input("Enter the third number : "))

if((iNo1 > iNo2) and (iNo1 > iNo3)):
    print(iNo1,"is maximum number")
elif((iNo2 > iNo1) and (iNo2 > iNo3)):
    print(iNo2,"is the Maximum number")
else:
    print(iNo3,"is maximum number")