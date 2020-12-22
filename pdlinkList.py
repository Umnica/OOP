from generalList import generalList
from pdlink import pdlink
# Процедуры для 1 Сделки
# Сделки для 1 проедуры
# Добавить процедуру к сделке
# Удалить сделку
# Удалить процедуру у сделки
class pdlinkList(generalList):
    def __init__(self, hospital, items, data=[]):
        super().__init__(hospital, pdlink, items, data)

    def getProcedureCodesByDeal(self, dealID):
        return [pdl.getProcedureCode() for pdl in self._list if pdl.getDealCode() == dealID]

    def getDealCodes(self, procedureID):
        return [pdl.getDealCode() for pdl in self._list if pdl.getProcedureCode() == procedureID]

    def appendProcedureID(self, dealID, procedureID):
        newlink = pdlink(dealID, procedureID)
        self.appendList(newlink)

    def removeDeal(self, dealID):
        for i in self._list:
            if i.getDealCode() == dealID:
                self._list.remove(i)

    def removeProcedureByDeal(self, dealID, procedureID):
        for i in self._list:
            if i.getDealCode() == dealID and i.getProcedureCode() == procedureID:
                self._list.remove(i)
