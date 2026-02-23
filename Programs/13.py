
iNo = int(input("Enter the number : "))
iMultiplication = 1

for i in range(1, ((iNo // 2)+1), +1):
    if(iNo % i == 0):
        iMultiplication = iMultiplication * i


print("The multiplication of factors of the given number is",iMultiplication)