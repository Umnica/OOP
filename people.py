from general import general


class people(general):
    def __init__(self, code='', name='', surname='', secname='', data={}):
        self.setName(name)
        self.setSurname(surname)
        self.setSecname(secname)
        super().__init__(code, data)

    def setName(self, value): self._name = value
    def setSurname(self, value): self._surname = value
    def setSecname(self, value): self._secname = value

    def getName(self): return self._name
    def getSurname(self): return self._surname
    def getSecname(self): return self._secname

    def __str__(self):
        s = '{0} {1} {2}'.format(self.getSurname(), self.getName(), self.getSecname())
        return s
