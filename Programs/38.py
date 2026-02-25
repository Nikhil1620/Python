iNo = int(input("Enter the number : "))
ifactorial = 1

for i in range(iNo, 0, -1):
    if(i % 2 == 0):
        ifactorial = ifactorial * i

print("The even factorial of",iNo,"is",ifactorial)
