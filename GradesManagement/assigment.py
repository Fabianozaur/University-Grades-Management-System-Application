from exeption import *


class Assigment:
    def __init__(self, AId, desc, dead):
        if AId is None:
            raise NoID_A("Assigment's ID can't be none")
        self._AId = AId
        self.Desc = desc
        self.Dead = dead


    @property
    def AId(self):
        return self._AId

    @property
    def Desc(self):
        return self._desc

    @property
    def Dead(self):
        return self._dead

    @Desc.setter
    def Desc(self, value):
        if len(value) < 3 or value is None:
            raise LengthError('The description of the assignment should have at least 3 characters')
        self._desc = value

    @Dead.setter
    def Dead(self, value):
        self._dead = value

    def __str__(self):
        return 'AssignmentID: '+str(self.AId)+'; Description: '+self.Desc+'; Deadline: Week '+str(self.Dead)


