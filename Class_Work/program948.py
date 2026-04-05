
def SumFactors(No):
    iSum = 0

    for i in range(1,(No//2)+1):
        if(No % i == 0):
            iSum = iSum + i
        return iSum
            

def main():
    Value = print("Enter the number : ")
    Value = int(input())

    iRet = 0

    iRet = SumFactors(Value)

    print("The addition of the factors of",Value,"is",iRet)

main()