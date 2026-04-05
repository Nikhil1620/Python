
def CheckPerfect(No):
    iSum = 0

    for i in range(1,(No//2)+1):
        if(No % i == 0):
            iSum = iSum + i
    return (iSum == No)

def main():
    Value = print("Enter the number : ")
    Value = int(input())

    iRet = 0

    iRet = CheckPerfect(Value)

    if(iRet == True):
        print("it is perfect number")
    else:
        print("it is not a perfect number")


main()