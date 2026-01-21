# Write a program which accept total marks & obtained marks from user and
# calculate percentage.

iTotalMarks = int(input("Enter the total marks : "))

iObtainedMarks = int(input("Enter the obtained marks : "))

iPercentage = float((iObtainedMarks / iTotalMarks) * 100)

print("The percentage is",iPercentage,"%")

