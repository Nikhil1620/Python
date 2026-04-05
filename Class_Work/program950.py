
def DisplayDigits(No):
    iDigit = 0
    iSum = 0

    while(No != 0):
        iDigit = No % 10
        print(iDigit, end = " ")
        No = No / 10       ## Issue

def main():
    print("Enter the number : ")
    Value = int(input())

    DisplayDigits(Value)

main()