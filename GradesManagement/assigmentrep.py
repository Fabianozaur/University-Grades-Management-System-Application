from assigment import *
from exeption import *
from UndoController import *



class AssigmentRep:
    def __init__(self,undoController):
        self._assigmentRep=[]
        self._undoController=undoController

    def addA(self,a):
        for i in range(len(self._assigmentRep)):
            if self._assigmentRep[i].AId==a.AId:
                raise DuplicateId('You already have this id!')
        undo=FunctionCall(self.removeA,a.AId)
        redo=FunctionCall(self.addA,a)
        op=CascadedOperation(Operation(undo,redo))
        self._undoController.recordOperation(op)
        self._assigmentRep.append(a)
    def removeA(self,id):
        ok=0
        for i in self._assigmentRep:
            if i.AId==id:
                ok=1
                undo = FunctionCall(self.removeA, i.AId)
                redo = FunctionCall(self.addA, i)
                op = CascadedOperation(Operation(redo, undo))
                self._undoController.recordOperation(op)
                self._assigmentRep.remove(i)
        if ok==0:
            raise NoID_A("The id you introduced is not in the list of assigments")
    def updatedesc(self,id,desc):
        ok = 0
        for i in self._assigmentRep:
            if i.AId == id:
                ok = 1
                undo=FunctionCall(self.updatedesc,i.AId,i.Desc)
                redo=FunctionCall(self.updatedesc,i.AId,desc)
                op = CascadedOperation(Operation(undo, redo))
                self._undoController.recordOperation(op)
                i.Desc=desc
        if ok == 0:
            raise NoID_A("The id you introduced is not in the list of assigments")
    def updatedead(self,id,dead):
        ok = 0
        for i in self._assigmentRep:
            if i.AId == id:
                ok = 1
                undo=FunctionCall(self.updatedead,i.AId,i.Dead)
                redo=FunctionCall(self.updatedead,i.AId,dead)
                op=CascadedOperation(Operation(undo,redo))
                self._undoController.recordOperation(op)
                i.Dead=dead
        if ok == 0:
            raise NoID_A("The id you introduced is not in the list of assigments")

    def givweek(self,id):
        for i in self._assigmentRep:
            if i.AId==id:
                return  i.Dead


    def listA(self):
        return self._assigmentRep

    def __len__(self):
        return len(self._assigmentRep)
    def __getitem__(self, item):
        return self._assigmentRep[item]

    # def update_string(self):
    #     for i in self._assigmentRep:
    #         if i.AId == id:
    #             for i in