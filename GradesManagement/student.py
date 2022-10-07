from exeption import *
class Student:
    def __init__(self,SId,name,group):
        if SId is None:
            raise NoID_S("Student ID can't be none")
        self._SId=SId
        self.Name=name
        self.Group=group
        
    @property
    def SId(self):
        return self._SId
    
    @property
    def Name(self):
        return self._name
    
    @property
    def Group(self):
        return self._group
    @Name.setter
    def Name(self,value):
        if len(value)<3 or value is None:
            raise NameError('The name should have at least 3 characters')
        self._name=value
    @Group.setter
    def Group(self,value):
        if value<911 or value >918 or value is None:
            raise GroupError('Group should be in the interval [912,917]')
        self._group=value
    def __str__(self):
        return "Student's Id: "+str(self.SId)+' ; Name: '+self.Name+' ; Group: '+str(self.Group)

    
    