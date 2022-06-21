class A:                                    #Single inheritance example.
    def displayA(self):
        print("Welcome to india.com A")

class B:                                     # dobble inheritance
    def displayB(self):
        print("welcome to india.com B")

class C(A,B):                                     # multi inheritance example
    def displayC(self):
        print("welcome to india.com C")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
