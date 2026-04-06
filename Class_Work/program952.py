
def SumDigits(No):
    iDigit = 0
    iSum = 0

    while(No != 0):
        iDigit = No % 10
        iSum = iSum + iDigit
        No = No // 10

    return iSum

def main():
    print("Enter the number : ")
    Value = int(input())

    iRet = SumDigits(Value)

    print("The addition of digits of ",Value,"is ",iRet)

main()