
def Summation(Brr):
    iSum = 0
    for i in Brr:
        iSum = iSum + i
    
    return iSum

def main():
    Size = 0
    Arr = []
    Value = 0

    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Arr.append(Value)

    Ret = Summation(Arr)

    print("The addition of the elements in the array is",Ret)

main()