
class Arithematic:
    ## Constructor
    def __init__(self,A = 0,B = 0):
        self.No1 = A     #Characteristics
        self.No2 = B     #Characteristics
    
    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans

    def Substraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans

    def Multiplication(self):
        Ans = 0
        Ans = self.No1 * self.No2
        return Ans
    
    def Division(self):
        Ans = 0
        Ans = self.No1 // self.No2
        return Ans

def main():
    aobj = Arithematic()

    Ret1 = aobj.Addition()
    print("Addition is",Ret1)

    Ret2 = aobj.Substraction()
    print("Substraction is",Ret2)
    

main()