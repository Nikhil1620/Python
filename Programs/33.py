iNo = int(input("Enter the number : "))
ifactorial = 1

for i in range(iNo, 0, -1):
    ifactorial = ifactorial * i

print("The factorial of",iNo,"is",ifactorial)
