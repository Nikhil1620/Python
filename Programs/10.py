iNo = int(input("Enter the number : "))

for i in range(1, (iNo//2)+1, +1):
    if(iNo % i == 0 and i % 2 == 0):
        print(i,end = " ")