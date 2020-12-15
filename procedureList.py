from generalList import generalList
from procedure import procedure


class procedureList(generalList):
    def __init__(self, hospital, items=None, data=[]):
        super().__init__(hospital, procedure, items, data)
    def getName(self, code): return self.findCode(code).getName()
    def getDoctor(self, code): return self.findCode(code).getDoctor()
    def getFullCost(self): return sum([p.getCost() for p in self._list])
