from patientList import patientList
from doctorList import doctorList
from procedureList import procedureList
from dealList import dealList
from deal import deal
from patient import patient
from doctor import doctor
from procedure import procedure
from hospital import hospital

deals = dealList()
patients = patientList()
doctors = doctorList()
procedures = procedureList()


doc1 = doctor(1, 'Ольга', 'Яновская', 'Андреевна','Психолог', 'высшая категория')
doc2 = doctor(2, 'Елена', 'Дорофеева', 'Борисовна', 'Психолог', '1 категория')
doctors.appendList(doc1)
doctors.appendList(doc2)

r1 = procedure(0,'тыкунть носом', 500, doc1)
r2 = procedure(0, 'консультация', 3500, doc2)
r3 = procedure(0, 'консультация2', 100, doc2)
procedures.appendList(r1)
procedures.appendList(r2)
procedures.appendList(r3)


p1 = patient(1, 'Кирилл', 'Вторцев', 'Дмитриевич', '21.11.2001', 50)
p2 = patient(2, 'Марк', 'Захаров', '', '08.05.2001', -90)
patients.appendList(p1)
patients.appendList(p2)


d1 = deal(1, '02.11.2020', 'что-то там 1', p1, [r1])
d2 = deal(2, '03.11.2020', 'что-то там 2', p2, [r1, r2])
d3 = deal(3, '11.11.2020', 'что-то там 3', p1, [r3])
#d1.setPatient(p1)
#d2.setPatient(p2)
deals.appendList(d1)
deals.appendList(d2)
deals.appendList(d3)
print(procedures)
