

class Protected:
    def __init__(self):
        self.__protectedVar = "Justin will"
        print(self.__protectedVar)

obj1 = Protected()
obj1.__protectedVar = "learn"
print(obj1.__protectedVar)

class Private:
    def __init__(self):
        self.__privateVar = "some"

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self,private):
        self.__privateVar = private


obj2 = Private()
obj2.setPrivate("Python")
obj2.getPrivate()

