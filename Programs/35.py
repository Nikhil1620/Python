
iNo = int(input("Enter the number : "))

for i in range((iNo*10), iNo-1, -1):
    if(i % iNo == 0):
        print(i, end = " ")