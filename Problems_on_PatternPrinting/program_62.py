# Accept number from user and display below pattern.
# Input : 5
# Output : 1 * 2 * 3 * 4 * 5 *

iNo = int(input("Enter the number : "))

i = 0

for i in range(1, iNo+1, 1):
    print(i, " * ", end = " ")