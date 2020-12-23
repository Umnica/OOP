from people import people


class patient(people):
    _props = ['_code', '_name', '_surname', '_secname', '_yearOfBirth', '_discount']

    def __init__(self, code='', name='', surname='', secname='', yearOfBirth='', discount=0, data={}):
        self.setYearOfBirth(yearOfBirth)
        self.setDiscount(discount)
        super().__init__(code, name, surname, secname, data)

    def setDiscount(self, value): self._discount = value
    def setYearOfBirth(self, value): self._yearOfBirth = value

    def getDiscount(self): return self._discount
    def getYearOfBirth(self): return self._yearOfBirth

    def __str__(self):
        s = '{0} {1} {2} {3}'.format(self.getSurname(), self.getName(), self.getSecname(), self.getYearOfBirth())
        return s
