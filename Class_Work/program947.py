
def DisplayFactors(No):
    for i in range(1,int((No/2)+1)):
        if(No % i == 0):
            print(i, end = " ")

def main():
    Value = print("Enter the number : ")
    Value = int(input())

    DisplayFactors(Value)

main()