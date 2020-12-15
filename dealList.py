from generalList import generalList
from deal import deal


class dealList(generalList):
    def __init__(self, hospital, items=None, data=[]):
        super().__init__(hospital, deal, items, data)
    def findByPatientCode(self, code):
        for l in self._list:
            p = l.getPatient()
            if p.getCode() == code:
                return p
    def findByDiagnosis(self, diagnosis):
        for l in self._list:
            if l.getDiagnosis() == diagnosis:
                return l
    def findByDate(self, date):
        for l in self._list:
            if l.getDate() == date:
                return l
