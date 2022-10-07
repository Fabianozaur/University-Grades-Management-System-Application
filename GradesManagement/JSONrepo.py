from studentrep import *
from student import *
from assigmentrep import *
from assigment import *
from graderep import *
from grade import *
import json


class RepoJSONStudents(StudentRep):
    def __init__(self,ud,filename):
        StudentRep.__init__(self,ud)
        self._filename=filename
        self._loadFromFile()
    def _saveFile(self):
        f = open(self._filename, "w")
        json.dump(self.listS(), f)
        f.close()
    def store(self,object):
        StudentRep.addS(self,object)
        self._saveFile()
    def addS(self,s):
        StudentRep.addS(self,s)
        self._saveFile()
    def removeS(self,id):
        StudentRep.removeS(self,id)
        self._saveFile()
    def updaten(self,newname,id):
        StudentRep.updaten(self,id,newname)
        self._saveFile()
    def updateg(self,id,newgroup):
        StudentRep.updateg(self,id,newgroup)
        self._saveFile()
    def _loadFile(self):
        result = []
        f = open(self._filename, "r")
        return json.load(f)
    def _loadFromFile(self):
        for obj in self._loadFile():
            self.store(obj)
class RepoJSONAssigments(AssigmentRep):
    def __init__(self,ud,filename):
        AssigmentRep.__init__(self,ud)
        self._filename=filename
        self._loadFromFile()

    def store(self,object):
        AssigmentRep.addA(self,object)
        self._saveFile()
    def _saveFile(self):
        f = open(self._filename, "w")
        json.dump(self.listA(), f)
        f.close()
    def addA(self,s):
        AssigmentRep.addA(self,s)
        self._saveFile()
    def removeA(self,id):
        AssigmentRep.removeA(self,id)
        self._saveFile()
    def updatedesc(self,newdesc,id):
        AssigmentRep.updatedesc(self,id,newdesc)
        self._saveFile()
    def updatedead(self,id,newdead):
        AssigmentRep.updatedead(self,id,newdead)
        self._saveFile()
    def _loadFile(self):
        result = []
        f = open(self._filename, "r")
        return json.load(f)
    def _loadFromFile(self):
        for obj in self._loadFile():
            self.store(obj)

class RepoJSONGrade(GradeRep):
    def __init__(self,ud,filename):
        GradeRep.__init__(self,ud)
        self._filename=filename
        self._loadFromFile()

    def store(self,object):
        GradeRep.addG(self,object)
        self._saveFile()
    def _saveFile(self):
        f = open(self._filename, "w")
        json.dump(self.listG(), f)
        f.close()
    def addG(self,s):
        GradeRep.addG(self,s)
        self._saveFile()
    def deleteGS(self,id):
        GradeRep.deleteGS(self,id)
        self._saveFile()
    def deleteGA(self,id):
        GradeRep.deleteGA(self,id)
        self._saveFile()
    def gradestud(self,ids,ida,grade):
        GradeRep.gradestud(self,ids,ida,grade)
        self._saveFile()
    def _loadFile(self):
        f = open(self._filename, "r")
        return json.load(f)
    def _loadFromFile(self):
        for obj in self._loadFile():
            self.store(obj)

