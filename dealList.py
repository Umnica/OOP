from generalList import generalList
from deal import deal


class dealList(generalList):
    def __init__(self, hospital, items=None, data=[]):
        super().__init__(hospital, deal, items, data)

    def findByPatientCode(self, code):
        for i in self._list:
            p = i.getPatient()
            if p.getCode() == code:
                return p

    def findByDiagnosis(self, diagnosis):
        for i in self._list:
            if i.getDiagnosis() == diagnosis:
                return i

    def findByDate(self, date):
        for i in self._list:
            if i.getDate() == date:
                return i
