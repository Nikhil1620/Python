iNo1 = int(input("Enter the first number : "))
iNo2 = int(input("Enter the Second number : "))
iNo3 = int(input("Enter the third number : "))

if(iNo1 > iNo2 and iNo1 > iNo3):
    print(iNo1,"is largest.")
elif(iNo2 > iNo1 and iNo2 > iNo3):
    print(iNo2,"is largest")
else:
    print(iNo3,"is largest")