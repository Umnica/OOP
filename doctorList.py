from generalList import generalList
from doctor import doctor


class doctorList(generalList):
    def __init__(self, hospital, items=None, data=[]):
        super().__init__(hospital, doctor, items, data)

    def getSpecialty(self, code): return self.findCode(code).getSpecialty()
    def getCategory(self, code): return self.findCode(code).getCategory()
