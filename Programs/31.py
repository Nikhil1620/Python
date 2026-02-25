
iNo1 = int(input("Enter the number : "))
iNo2 = int(input("Enter the number of multiples want to display : "))

for i in range(1, (iNo1*iNo2) + 1, +1):
    if(i % iNo1 == 0):
        print(i, end = " ")