class Student:
    __name="Ravi"                       #private variable will be access with functions
    def __init__(self):
        print(self.__name)              #FUNCTION
        self.__displayinfo()                # private variable can not be access
    def __displayinfo(self):                # FUNCTION
        print("welcome to india.com")


obj=Student()
