#
import uuid


class general:
    # свойства, к. будут сох. т загр.
    _props = ['_code']
    def __init__(self, code='', data={}):
        self._hospital = None
        if code:
            self.setCode(code)
        else:
            self.setCode(general.generateCode())
        # Загрузка сохр-ых св-в объекта
        for key in self.__class__._props:
            if key in data:
                setattr(self, key, data[key])

    @staticmethod
    def generateCode():
        return uuid.uuid1().hex

    def setCode(self, value): self._code = value

    def getCode(self): return self._code
    def setHospital(self, value): self._hospital = value


    # воз. словарь пропса
    def __iter__(self):
        for key in self.__class__._props:
            yield (key, getattr(self, key))
