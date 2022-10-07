from grade import *
from UndoController import *
class GradeRep:
    def __init__(self,undoController):
        self._gradeRepo=[]
        self._UndoController=undoController
    def addG(self,g):
        res = []
        self._gradeRepo.append(g)
        #undo = FunctionCall(self.addG, i)
        #redo = FunctionCall(self.deleteGS, i.SId)
        #op = CascadedOperation(Operation(undo, redo))
        #res.append(op)
        #return res
    def listG(self):
        return self._gradeRepo
    def __len__(self):
        return len(self._gradeRepo)
    def __getitem__(self, item):
        return self._gradeRepo[item]

    def deleteGS(self,ids):
        res=[]
        remove=[]
        for i in self._gradeRepo:
            if i.SId==ids:
                remove.append(i)
        for i in remove:
                undo = FunctionCall(self.addG, i)
                redo = FunctionCall(self.deleteGS, i.SId)
                op = CascadedOperation(Operation(undo, redo))
                res.append(op)
                self._gradeRepo.remove(i)
        return res
    def deleteGA(self,ida):
        res=[]
        remove=[]
        for i in self._gradeRepo:
            if i.AId==ida:
                remove.append(i)
        for i in remove:
            undo = FunctionCall(self.addG, i)
            redo = FunctionCall(self.deleteGA, i.AId)
            op = CascadedOperation(Operation(undo, redo))
            res.append(op)
            self._gradeRepo.remove(i)
        return res


    def gradestud(self,ids,ida,gr):
        ok = 0
        for i in self._gradeRepo:
            if i.SId == ids and i.AId == ida:
                if i.GradeV == 0:
                    i.GradeV = gr
                    undo = FunctionCall(self.gradestud, i.SId,i.AId,i.GradeV)
                    redo = FunctionCall(self.gradestud,i.SId, i.AId, gr)
                    op = CascadedOperation(Operation(undo, redo))
                    self._UndoController.recordOperation(op)
                    ok = 1
                    break
                else:
                    raise GradeError("The grade can not be modified after it was given")
        if ok == 0:
            raise GradeError('The student you selected does not have the assigment you selected')
    def getstud(self,ida):
        l=[]
        ok=0
        for i in self._gradeRepo:
            if i.AId==ida and i.GradeV !=0:
                l.append(i.SId)
                l.append(i.GradeV)
            if i.GradeV==0:
                ok=1
        else:
            if  not l:
                if ok==0:
                    raise GradeError('The assigment you introduced was not given to any of the students')
                else:
                    raise GradeError('The students which have that assignment are currently ungraded')
            else:
                return l







