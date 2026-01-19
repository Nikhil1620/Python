# Accept two numbers from user and display first number in second number of times.
 
iNo1 = int(input("Enter the First number :"))
iNo2 = int(input("Enter the Second number :"))

iCnt = 0

for iCnt in range(0, iNo2, 1):
    print(iNo1, end = " ")