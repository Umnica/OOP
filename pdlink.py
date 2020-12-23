from general import general


class pdlink(general):
    _props = ['_code', '_dealID', '_procedureID']

    def __init__(self, deal=None, procedure=None, data={}):
        if isinstance(deal, str):
            self.setDealCode(deal)
        elif issubclass(deal.__class__, general):
            self.setDeal(deal)
        elif not '_dealID' in data:
            raise TypeError("Неверно указан тип сделки.(Должен быть str/general)", deal)

        if isinstance(procedure, str):
            self.setProcedureCode(procedure)
        elif issubclass(procedure.__class__, general):
            self.setProcedure(procedure)
        elif not '_procedureID' in data:
            raise TypeError("Неверно указан тип сделки.(Должен быть str/general)", procedure)
        super().__init__('', data)
        self._code = self._dealID + self._procedureID


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
