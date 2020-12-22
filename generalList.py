class generalList:
    def __init__(self, hospital, itemClass, items=None, data=[]):
        self._hospital = hospital
        if items:
            self._list = items
        elif len(data):
            self._list = [itemClass(data=d) for d in data]
        else:
            self._list = []
        for i in self._list:
            i.setHospital(self._hospital)

    def clear(self): self._list.clear()

    def findCode(self, code):
        for i in self._list:
            if i.getCode() == code:
                return i

    def getCodes(self): return [s.getCode() for s in self._list]
    def appendList(self, value):
        value.setHospital(self._hospital)
        self._list.append(value)


    def removeList(self, code):
        for s in self._list:
            if s.getCode() == code:
                self._list.remove(s)
    def __str__(self):
        return ',\n'.join([str(k) for k in self._list])

    # для вывода значений на экран
    def listOfStr(self):
        return [str(i) for i in self._list]

    # для сохранения значений
    def listDicts(self):
        return [dict(i) for i in self._list]
