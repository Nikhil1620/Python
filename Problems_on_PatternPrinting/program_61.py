# Accept number from user and display below pattern.
# Input : 5
# Output : 5 # 4 # 3 # 2 # 1 #

iNo = int(input("Enter the number : "))

for i in range(iNo, 0, -1):
    print(iNo," # ",end = "")
    iNo = iNo - 1