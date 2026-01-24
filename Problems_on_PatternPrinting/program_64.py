# Accept number from user and display below pattern.
# Input : 8
# Output : 2 4 6 8 10 12 14 16 

iNo = int(input("Enter the number : "))

i = 0

for i in range(1, (iNo*2) + 1, 1):
    if(i % 2 == 0):
        print(i, end = " ")