from general import general


class procedure(general):
    _props = ['_code', '_name', '_cost', '_doctorID']
    def __init__(self, code='', name='', cost=0, doctor=None, data={}):
        self.setName(name)
        self.setCost(cost)
        if doctor:
            self.setDoctor(doctor)
        super().__init__(code, data)

    def setHospital(self, value): self._hospital = value
    def setName(self, value): self._name = value
    def setCost(self, value): self._cost = value
    def setDoctor(self, value): 
        self._doctorID = value.getCode()


    def getName(self): return self._name
    def getCost(self): return self._cost
    def getDoctor(self):
        doc = self._hospital.getDoctors().findCode(self._doctorID)
        return doc

    def getDoctorID(self): return self._doctorID

    def __str__(self):
        s = '{0}, {1}, {2}'
        s = s.format(self._name, self._cost, str(self.getDoctor()))
        return s
