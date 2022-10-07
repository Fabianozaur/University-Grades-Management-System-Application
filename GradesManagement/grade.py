from exeption import *

class Grade:
    def __init__(self,sId,aId,gradev):
        if sId is None:
            raise NoID_G('Student id cannot be none')
        if sId is None:
            raise NoID_G('Assignment id cannot be none')
        self._sId=sId
        self._aId=aId
        self.GradeV = gradev

    @property
    def SId(self):
        return self._sId

    @property
    def AId(self):
        return self._aId

    @property
    def GradeV(self):
        return self._gradeV
    @GradeV.setter
    def GradeV(self,value):
        if value <0 or value >10 or value is None:
            raise GradeError('Grade cannot be outside the interval [0,10]')
        self._gradeV=value
    def __str__(self):
        if self.GradeV==0:
            return 'The Student with the Id: ' + str(self.SId) + ' has to do Assignment id: ' + str(self.AId) + '; He is curently ungraded'
        else:
            return 'The Student with the Id: '+str(self.SId)+' has to do Assignment id: '+str(self.AId)+' ;His curent grade is '+str(self.GradeV)

