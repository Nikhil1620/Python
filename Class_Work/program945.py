
def CheckEven(No):
    if(No % 2 == 0):
        print("Even")
    else:
        print("Odd")


def main():
    Value = print("Enter the number : ")
    Value = int(input())

    CheckEven(Value)

main()