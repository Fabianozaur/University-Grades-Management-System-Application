from studentrep import *
from student import *
from assigmentrep import *
from assigment import *
from graderep import *
from grade import *






class RepoTextStudents(StudentRep):
    def __init__(self,ud,filename):
        StudentRep.__init__(self,ud)
        self._filename=filename
        self._loadFile()

    def store(self,object):
        StudentRep.addS(self,object)
        self._saveFile()
    def _saveFile(self):
        f=open(self._filename,'w')
        for i in self.listS():
            f.write(str(i.SId)+';'+i.Name+';'+str(i.Group)+'\n')
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
        f=open(self._filename,'r')
        f1=f.readlines()
        for line in f1:
            line=line.split(';')
            lo=line[2][:len(line[2])-1]
            student=Student(int(line[0]),line[1],int(lo))
            self.store(student)

class RepoTextAssigments(AssigmentRep):
    def __init__(self,ud,filename):
        AssigmentRep.__init__(self,ud)
        self._filename=filename
        self._loadFile()
    def store(self,object):
        AssigmentRep.addA(self,object)
        self._saveFile()
    def _saveFile(self):
        f=open(self._filename,'w')
        for i in self.listA():
            f.write(str(i.AId)+';'+i.Desc+';'+str(i.Dead)+'\n')
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
        f=open(self._filename,'r')
        f1=f.readlines()
        for line in f1:
            line=line.split(';')
            lo=line[2][:len(line[2])-1]
            assign=Assigment(int(line[0]),line[1],int(lo))
            self.store(assign)

class RepoTextGrade(GradeRep):
    def __init__(self,ud,filename):
        GradeRep.__init__(self,ud)
        self._filename=filename
        self._loadFile()

    def store(self,object):
        GradeRep.addG(self,object)
        self._saveFile()
    def _saveFile(self):
        f=open(self._filename,'w')
        for i in self.listG():
            f.write(str(i.SId)+';'+str(i.AId)+';'+str(i.GradeV)+'\n')
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
        f=open(self._filename,'r')
        f1=f.readlines()
        for line in f1:
            line=line.split(';')
            lo=line[2][:len(line[2])-1]
            grade=Grade(int(line[0]),int(line[1]),int(lo))
            self.store(grade)

