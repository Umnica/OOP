from general import general


class pdlink(general):
    _props = ['_code', '_dealID', '_procedureID']
    def __init__(self, deal=None, procedure=None, data={}):
        if isinstance(deal, str):
            self.setDealCode(deal)
        elif issubclass(deal, general):
            self.setDeal(deal)
        else:
            raise TypeError("Неверно указан тип сделки.(Должен быть str/general)", deal)

        if isinstance(procedure, str):
            self.setProcedureCode(procedure)
        elif issubclass(procedure, general):
            self.setProcedure(procedure)
        else:
            raise TypeError("Неверно указан тип сделки.(Должен быть str/general)", Procedure)
        code = self._dealID + self._procedureID
        super().__init__(code, data)


    def setDeal(self, value):
        self._dealID = value.getCode()
    def setProcedure(self, value):
        self._procedureID = value.getCode()
    def setProcedureCode(self, value):
        self._procedureID = value
    def setDealCode(self, value):
        self._dealID = value

    def getDeal(self):
        return self._hospital.getDeal(self._dealID)
    def getProcedure(self):
        return self._hospital.getProcedure(self._pocedureID)
    def getDealCode(self):
        return self._dealID
    def getProcedureCode(self):
        return self._procedureID
