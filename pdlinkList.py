from generalList import generalList
from pdlink import pdlink

# Процедуры для 1 Сделки
# Сделки для 1 проедуры
# Добавить процедуру к сделке
# Удалить сделку
# Удалить процедуру у сделки
class pdlinkList(generalList):
    def __init__(self, hospital, items=[], data=[]):
        super().__init__(hospital, pdlink, items, data)

    def getProcedureCodesByDeal(self, dealID):
        return [pdl.getProcedureCode() for pdl in self._list if pdl.getDealCode() == dealID]

    def getDealCodes(self, procedureID):
        return [pdl.getDealCode() for pdl in self._list if pdl.getProcedureCode() == procedureID]

    def appendLink(self, dealID, procedureID):
        newlink = pdlink(dealID, procedureID)
        if not self.findCode(newlink.getCode()):
            self.appendList(newlink)

    def removeDeal(self, dealID):
        codes = []
        for i in self._list:
            if i.getDealCode() == dealID:
                codes.append(i.getCode())
                self._list.remove(i)
        return codes

    def removeProcedureByDeal(self, dealID, procedureID):
        codes = []
        for i in self._list:
            if i.getDealCode() == dealID and i.getProcedureCode() == procedureID:
                codes.append(i.getCode())
                self._list.remove(i)
        return codes
