iNo = int(input("Enter the number : "))

for i in range(1, ((iNo*2)+1), +1):
    if(i % 2 == 0):
        print(i,end = " ")