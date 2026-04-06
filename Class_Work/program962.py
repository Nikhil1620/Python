
def Max(Brr):
    iMax = Brr[0]
    for i in range(len(Brr)):
        if(iMax < Brr[i]):
            iMax = Brr[i]
    
    return iMax

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

    Ret = Max(Arr)

    print("The maximum element of the given list is",Ret)

main()