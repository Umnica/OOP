from deal import deal
from patient import patient
from doctor import doctor
from procedure import procedure
from hospital import hospital


def changeItems():
    doc3 = doctor('3', 'Наталия', 'Чехонина', 'Павловна', 'стоматолог', '1 категория')
    h.appendDoctor(doc3)
    r3 = procedure('3', 'консультация', 500, doc3)
    h.appendProcedure(r3)
    p2 = patient('2', 'Марк', 'Захаров', '', '08.05.2001', -90)
    h.appendPatient(p2)
    d3 = deal('3', '13.12.2020', 'Зубной налет', p2, [r3])
    h.appendDeal(d3)


def changeItems2():
    h.removeDoctor('3')
    h.removeProcedure('3')
    h.removeDeal('3')


def main1():
    h = hospital()
    h.connectDb('db.sqlite3')
    h.dbLoad()
    #changeItems()
    changeItems2()
    h.save('dbSave.json')
    h.dbSave()


def main2():
    h = hospital()
    h.connectDb('db1.sqlite3')
    h.load('res.json')
    h.dbSave()


main2()
