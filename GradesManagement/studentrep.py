from student import *
from exeption import *
from UndoController import *

class StudentRep:
    def __init__(self,undoController):
        self._studentRep=[]
        self._undoController=undoController

    def addS(self,s):
        for i in range(len(self._studentRep)):
            if self._studentRep[i].SId==s.SId:
                raise DuplicateId('You already have this id!')
        undo=FunctionCall(self.removeS,s.SId)
        redo=FunctionCall(self.addS,s)
        op=CascadedOperation(Operation(undo,redo))
        self._undoController.recordOperation(op)
        self._studentRep.append(s)
    def removeS(self,id):
        ok=0
        for i in self._studentRep:
            if i.SId==id:
                ok=1
                undo = FunctionCall(self.removeS, i.SId)
                redo = FunctionCall(self.addS, i)
                op = CascadedOperation(Operation(redo,undo))
                self._undoController.recordOperation(op)
                self._studentRep.remove(i)
        if ok==0:
            raise NoID_S("The id you introduced is not in the list of students")
    def updaten(self,id,name):
        ok = 0
        for i in self._studentRep:
            if i.SId == id:
                ok = 1
                undo = FunctionCall(self.updaten, i.SId, i.Name)
                redo = FunctionCall(self.updaten, i.SId, name)
                op = CascadedOperation(Operation(undo, redo))
                self._undoController.recordOperation(op)
                i.Name=name
        if ok == 0:
            raise NoID_S("The id you introduced is not in the list of students")
    def updateg(self,id,group):
        ok = 0
        for i in self._studentRep:
            if i.SId == id:
                ok = 1
                undo = FunctionCall(self.updateg, i.SId, i.Group)
                redo = FunctionCall(self.updateg, i.SId, group)
                op = CascadedOperation(Operation(undo, redo))
                self._undoController.recordOperation(op)
                i.Group=group
        if ok == 0:
            raise NoID_S("The id you introduced is not in the list of students")
    def gividname(self,id):
        for i in self._studentRep:
            if i.SId==id:
                return i.Name


    def listS(self):
        return self._studentRep

    def __len__(self):
        return len(self._studentRep)
    def __getitem__(self, item):
        return self._studentRep[item]
