from patientList import patientList
from doctorList import doctorList
from procedureList import procedureList
from dealList import dealList
from deal import deal
from patient import patient
from doctor import doctor
from procedure import procedure
import json
import sqlite3

class hospital:
    def __init__(self):
       self.__patients = patientList(self)
       self.__doctors = doctorList(self)
       self.__procedures = procedureList(self)
       self.__deals = dealList(self)


    def connectDb(self, file):
        self._connection = sqlite3.connect(file)
        self._cursor = self._connection.cursor()

    def getPatients(self): return self.__patients
    def getDoctors(self): return self.__doctors
    def getProcedures(self): return self.__procedures
    def getDeals(self): return self.__deals

    def getPatient(self, code): return self.__patients.findCode(code)
    def getDoctor(self, code): return self.__doctors.findCode(code)
    def getProcedure(self, code): return self.__procedures.findCode(code)
    def getDeal(self, code): return self.__deals.findCode(code)

    def appendPatient(self, patient): self.__patients.appendList(patient)
    def appendDoctor(self, doctor): self.__doctors.appendList(doctor)
    def appendProcedure(self, procedure): self.__procedures.appendList(procedure)
    def appendDeal(self, deal): self.__deals.appendList(deal)

    def removePatient(self, code):
        if self._connection:
            self.__delete_row('patient', code)
        self.__patients.removeList(code)
    def removeDoctor(self, code):
        if self._connection:
            self.__delete_row('doctor', code)
        self.__doctors.removeList(code)
    def removeProcedure(self, code):
        if self._connection:
            self.__delete_row('procedure', code)
        self.__procedures.removeList(code)
    def removeDeal(self, code):
        if self._connection:
            self.__delete_row('deal', code)
        self.__deals.removeList(code)

    def save(self, file):
        res = {
            'Patients': self.__patients.listDicts(),
            'Doctors': self.__doctors.listDicts(),
            'Procedures': self.__procedures.listDicts(),
            'Deals': self.__deals.listDicts()
        }
        fileW = open(file, 'w', encoding="utf-8")
        json.dump(res, fileW, indent=4, ensure_ascii=False)
        fileW.close()

    def load(self, file):
        fileR = open(file, 'r', encoding="utf-8")
        data = json.load(fileR)
        fileR.close()

        if 'Patients' in data:
            self.__patients = patientList(self, data=data['Patients'])
        if 'Doctors' in data:
            self.__doctors = doctorList(self, data=data['Doctors'])
        if 'Procedures' in data:
            self.__procedures = procedureList(self, data=data['Procedures'])
        if 'Deals' in data:
            self.__deals = dealList(self, data=data['Deals'])

    def dbLoad(self):
        patientRecs = self.__get_table('patient')
        self.__patients = patientList(self, data=patientRecs)

        doctorRecs = self.__get_table('doctor')
        self.__doctors = doctorList(self, data=doctorRecs)

        procedureRecs = self.__get_table('procedure')
        self.__procedures = procedureList(self, data=procedureRecs)

        dealRecs = self.__get_table('deal')
        self.__deals = dealList(self, data=dealRecs)

    def dbSave(self):
        for p in self.__patients.listDicts():
            self.__post_row('patient', p)
            self._connection.commit()
        for d in self.__doctors.listDicts():
            self.__post_row('doctor', d)
            self._connection.commit()
        for pr in self.__procedures.listDicts():
            self.__post_row('procedure', pr)
            self._connection.commit()
        for de in self.__deals.listDicts():
            self.__post_row('deal', de)
            self._connection.commit()

    def __get_table(self, tablename):
        sqlite_select_query = 'SELECT * from '+tablename

        cursor = self._connection.cursor()
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        if 'patient' == tablename:
            itemClass = patient
        if 'doctor' == tablename:
            itemClass = doctor
        if 'procedure' == tablename:
            itemClass = procedure
        if 'deal' == tablename:
            itemClass = deal

        return [dict(zip(itemClass._props, d)) for d in records]

    def __post_row(self, tablename, itemDict):
        keys = ','.join(itemDict.keys())
        question_marks = ','.join(list('?'*len(itemDict)))
        values = tuple([hospital.formatIDList(v) for v in itemDict.values()])

        self._connection.execute('INSERT OR REPLACE INTO '+tablename+' ('+keys+') VALUES ('+question_marks+')', values)

    def __delete_row(self, tablename, code):
        sql_remove_query = 'DELETE FROM '+tablename+' WHERE _code = \''+str(code)+'\''
        self._cursor.execute(sql_remove_query)

    @staticmethod
    def formatIDList(ls):
        if isinstance(ls, list):
            strFormatting = (lambda s: s if isinstance(s, str) else s)
            return 'ARRAY'+str([strFormatting(i) for i in ls])
        else:
            return ls
