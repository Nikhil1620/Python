iNo = int(input("Enter the number : "))

for i in range((iNo//2)+1, 0, -1):
    if(iNo % i != 0):
        print(i,end = " ")