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
        s = '{0} {1} {2} {3} {4}'.format(self.getSurname(), self.getName(), self.getSecname(), self.getSpecialty(), self.getCategory())
        return s
