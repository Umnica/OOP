from deal import deal
from patient import patient
from doctor import doctor
from procedure import procedure
from hospital import hospital

h = hospital()
h.connectDb('db.sqlite3')
doc1 = doctor('1', 'Ольга', 'Яновская', 'Андреевна', 'Психолог', 'высшая категория')
doc2 = doctor('2', 'Елена', 'Дорофеева', 'Борисовна', 'Психолог', '1 категория')
h.appendDoctor(doc1)
h.appendDoctor(doc2)


r1 = procedure('1', 'тыкнуть носом', 50, doc1)
r2 = procedure('2', 'консультация', 350, doc2)
h.appendProcedure(r1)
h.appendProcedure(r2)


p1 = patient('1', 'Кирилл', 'Вторцев', 'Дмитриевич', '21.11.2001', 50)
p2 = patient('2', 'Марк', 'Захаров', '', '08.05.2001', -90)
h.appendPatient(p1)
h.appendPatient(p2)


d1 = deal('1', '02.11.2020', 'что-то там 1', p1, [r1])
d2 = deal('2', '03.11.2020', 'что-то там 2', p2, [r1, r2])


h.appendDeal(d1)
h.appendDeal(d2)
h.save('a.json')
#h.dbSave()
h.save('res.json')