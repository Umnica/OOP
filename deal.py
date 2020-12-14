from general import general
from procedureList import procedureList


class deal(general):
    _props = ['_code', '_date', '_diagnosis', '_patientID', '_procedureIDs']

    def __init__(self, code='', date='', diagnosis='', patient=None, procedures=[], data={}):
        self.setDate(date)
        self.setDiagnosis(diagnosis)
        if patient:
            self.setPatient(patient)
        self._procedureIDs = [p.getCode() for p in procedures]
        super().__init__(code, data)

    def __str__(self):
        psS = ', '.join([('{' + str(p) + '}')for p in self.__getProcedures()])

        s = '{0}, {1}, {2}, {3}, [{4}]'
        s = s.format(self._date, self._diagnosis, self.getCostOfTreatment(), str(self.getPatient()), psS)
        return s

    def getCostOfTreatment(self):
        fullCost = self.getFullCostProcedures()
        discount = self.getPatient().getDiscount()
        if discount:
            return fullCost * (100 - discount) / 100
        else:
            return fullCost

    def setPatient(self, patient): self._patientID = patient.getCode()
    def setDate(self, value): self._date = value
    def setDiagnosis(self, value): self._diagnosis = value

    def getPatient(self):
         return self._hospital.getPatient(self._patientID)
    def getDate(self): return self._date
    def getDiagnosis(self): return self._diagnosis

    def __getProcedures(self):
        return [self._hospital.getProcedure(code) for code in self._procedureIDs]
    def clearProcedures(self): self._procedureIDs.clear()
    def findProcedureCode(self, code):
        if code in self._procedureIDs:
            return self._hospital.getProcedure(code)

    def getProcedureCodes(self): return self._procedureIDs
    def appendProcedure(self, procedure): self._procedureIDs.append(procedure.getCode())
    def removeProcedure(self, code): self._procedureIDs.remove(code)

    def getFullCostProcedures(self):
        return sum([p.getCost() for p in self.__getProcedures()])
