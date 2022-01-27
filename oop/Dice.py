import random
from dataclasses import dataclass

from scipy import rand

@dataclass
class Die:
    __value:int = 1
    @property
    def value(self):
        return self.__value
    
    def roll(self):
        self.__value = random.randrange(1,7)

class Dice:
    def __init__(self) -> None:
        self.__list=[]
    
    @property
    def list(self):
        return tuple(self.__list)
    
    def addDie(self, die):
        self.__list.append(die)
    
    def rollAll(self):
        for die in self.__list:
            die.roll()

    def __iter__(self):
        for die in self.__list:
            yield die


def main():
    d1 = Die()
    d2 = Die()

    dc = Dice()
    dc.addDie(d1)
    dc.addDie(d2)

    dc.rollAll()

    print(dc.list[0].value,dc.list[1].value)

    print("+ +"*20)
    for d in dc:
        print(d.value)

if (__name__ == "__main__"):
    main()
