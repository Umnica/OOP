from generalList import generalList
from patient import patient


class patientList(generalList):
    def __init__(self, items=None, data=[]):
        super().__init__(patient, items, data)
    def getYearOfBirth(self, code): return self.findCode(code).getYearOfBirth()

