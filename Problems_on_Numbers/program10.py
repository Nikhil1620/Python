#Accept one number from user and print that number of * on screen.

iNo = int(input("Enter the number : "))

iCnt = 0

for iCnt in range(0, iNo, 1):
    print("*", end =" ")