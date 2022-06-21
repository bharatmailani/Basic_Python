class DemoClass:
    a=10
    def __init__(self):
        print("Welcome to India.com.")

    def showvalue(self):
        self.c=self.a*self.a
        print(self.c)

    def showvalue1(self):
        print("Welcome to India.com.")

    def showvalue2(self):
        self.c=self.a+self.a
        print(self.c)

    def showvalue3(self,a,b,c):
        print(a+b+c)


obj=DemoClass()
obj.showvalue()
obj.showvalue1()
obj.showvalue2()
obj.showvalue3(50,30,40)



