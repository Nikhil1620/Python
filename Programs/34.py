
iNo = int(input("Enter the number : "))

for i in range(iNo, (iNo*10)+1, +1):
    if(i % iNo == 0):
        print(i, end = " ")