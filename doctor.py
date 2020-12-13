from people import people


class doctor(people):
    _props = ['_code', '_name', '_surname', '_secname', '_specialty', '_category']

    def __init__(self, code='', name='', surname='', secname='', specialty='', category='', data={}):
        self.setSpecialty(specialty)
        self.setCategory(category)
        super().__init__(code, name, surname, secname, data)

    def setSpecialty(self, value): self._specialty = value
    def setCategory(self, value): self._category = value
    def getSpecialty(self): return self._specialty
    def getCategory(self): return self._category

    def __str__(self):
        s = self.getSurname()
        if self.getName():
            s += ' {0}'.format(self.getName())
        if self.getSecname():
            s += ' {0}'.format(self.getSecname())
        if self.getSpecialty():
            s += ' {0}'.format(self.getSpecialty())
        if self.getCategory():
            s += ' {0}'.format(self.getCategory())
        return s
