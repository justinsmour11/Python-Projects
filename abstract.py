
from abc import ABC, abstractmethod

class Guitar(ABC):
    def myGuitar(self, brand):
        print("I have an ", brand)

    @abstractmethod
    def location(self, brand):
        pass

class WhereIsGuitar(Guitar):
    def location(self, brand):
        print("My {} is in my closet.".format(brand))

obj = WhereIsGuitar()
obj.myGuitar("Ibanez")
obj.location("Ibanez")
