
def Min(Brr):
    iMin = Brr[0]
    for i in range(len(Brr)):
        if(iMin > Brr[i]):
            iMin = Brr[i]
    
    return iMin

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

    Ret = Min(Arr)

    print("The minimum element of the given list is",Ret)

main()