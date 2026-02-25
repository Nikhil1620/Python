iNo = int(input("Enter the number : "))

print("The odd numbers:")

for i in range(1, iNo+1, +1):
    if(i % 2 != 0):
        print(i,end = " ")