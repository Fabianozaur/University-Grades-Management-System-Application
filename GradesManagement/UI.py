from service import *



class UI:

    def __init__(self,service,undoRedo,repo):
        self._service=service
        self.undoRedo=undoRedo
        self._repository=repo
    def printMenu(self):
        print('-----')
        print('Menu: ')
        print('1.Manage student or assigment')
        print('2.Give assigment')
        print('3.Grade student')
        print('4.Statistics')
        print("5.Undo")
        print('6.Redo')
        print('0.Exit')

    def printGive(self):
        print('---------')
        print('1. Give an assignment to a student')
        print('2. Give an assignment to a group of students')

    def printEditStud(self):
        print('------')
        print('1.Add')
        print('2.Remove')
        print('3.Update name')
        print('4.Update groupe')
        print('5.List')

    def printEditAss(self):
        print('------')
        print('1.Add')
        print('2.Remove')
        print('3.Update description')
        print('4.Update deadline')
        print('5.List')

    def printstats(self):
        print('--------')
        print('1.List students along their assigments')
        print('2.List all students who received a given assignment, ordered by average grade for that assignment.')
        print('3.List all students who are late in handing in at least one assignment')
        print('4.List Students with the best school situation')

    def adds_ui(self):
        print("Insert the Id for the new student: ")
        id=input('>')
        print("Insert the name of the new student: ")
        name=input('>')
        print("Insert the group of the new student")
        group=input('>')
        s=self._service
        try:
            s.service_addS(id,name,group)
        except Exception as E:
            print(str(E))
    def remove_ui(self):
        s=self._service
        print("Insert the Id of the student you want to remove:")
        id=input('>')
        try:
            s.service_removeS(id)
        except  Exception as x:
            print(str(x))
    def updaten_ui(self):
        s=self._service
        print("Insert the Id of the student you want to update:")
        id=input('>')
        print("Insert the new name of the student: ")
        name=input('>')
        try:
            s.service_updaten(id,name)
        except  Exception as x:
            print(str(x))
    def updateg_ui(self):
        s=self._service
        print("Insert the Id of the student you want to update:")
        id=input('>')
        print("Insert the new group of the student: ")
        group=input('>')
        try:
            s.service_updateg(id,group)
        except  Exception as x:
            print(str(x))

    def adda_ui(self):
        s=self._service
        print("Insert the Id for the new assignment: ")
        id=input('>')
        print("Insert the description of the new assignment: ")
        desc=input('>')
        print("Insert the deadline of the new assignment")
        dead=input('>')
        try:
            s.service_addA(id,desc,dead)
        except Exception as E:
            print(str(E))
    def aremove_ui(self):
        s=self._service
        print("Insert the Id of the assignment you want to remove:")
        id=input('>')
        try:
            s.service_removeA(id)
        except  Exception as x:
            print(str(x))
    def updatedesc_ui(self):
        s=self._service
        print("Insert the Id of the assignment you want to update:")
        id=input('>')
        print("Insert the new description for the assignment: ")
        desc=input('>')
        try:
            s.service_updatedesc(id,desc)
        except  Exception as x:
            print(str(x))
    def updatedead_ui(self):
        s=self._service
        print("Insert the Id of the assignment you want to update:")
        id=input('>')
        print("Insert the new deadline for the assignment: ")
        dead=input('>')
        try:
            s.service_updatedead(id,dead)
        except  Exception as x:
            print(str(x))
    def givestud_ui(self):
        s=self._service
        print('Insert the id of the assignment you want to give ')
        id1=input('>')
        print('Insert the id of the student you want to receive the assignment ')
        id2 = input('>')
        try:
            s.givestud(id1,id2)
        except Exception as x:
            print(str(x))
    def givegroup_ui(self):
        s=self._service
        print('Insert the id of the assigment you want to give ')
        id=input('>')
        print('Insert the group that you want to receive the assignment')
        gr=input('>')
        try:
            s.givegroup(id,gr)
        except Exception as x:
            print(str(x))
    def gradestud_ui(self):
        s=self._service
        print("Insert the id of the student you want to grade")
        ids=input('>')
        print('Insert the id of the assigment you are giving a grade to')
        ida=input('>')
        print('Insert the grade ')
        gr=input('>')
        try:
            s.service_gradestud(ids,ida,gr)
        except Exception as x:
            print(str(x))
    def liststudents_ui(self):
        s=self._service
        print('Insert the id of the assigment you want to see the students ascending by their grades')
        ida=input('>')
        try:
            v=(s.service_liststud(ida))
            print('The list of students sorted by their grade on assigment:'+ida)
            print('')
            for i in v:
                print(str(i))

        except Exception as x:
            print(str(x))
    def late_ui(self):
        s=self._service
        print('Insert the current week: ')
        week=input('>')
        try:
            v=(s.service_late(week))
            print("The list with students that are late with at least one of their assignments")
            for i in v:
                print(i)
        except Exception as x:
            print(str(x))
    def best_ui(self):
        s=self._service
        try:
            r=s.service_best()
            print("The students sorted in descending order by average grade")
            for i in r:
                print(str(i))
        except Exception as x:
            print(str(x))
    def Start(self):
        if self._repository == "inmemory":
            self._service.initS()
            self._service.initA()
            self._service.initG()
        liststud=self._service._students.listS()
        for i in liststud:
            print(i)
        listass = self._service._assign.listA()
        for i in listass:
            print(i)
        listgr = self._service._grades.listG()
        for i in listgr:
            print(i)
        while True:
            self.printMenu()
            choice=input(">")
            if choice == '1':
                print('1. Manage students')
                print('2. Manage assignments')
                choice2=input('>')
                if choice2 =='1':
                    self.printEditStud()
                    choice3=input('>')
                    if choice3 =='1':
                        self.adds_ui()

                    elif choice3=='5':
                        liststud = self._service._students.listS()
                        for i in liststud:
                            print(i)
                    elif choice3=='2':
                        self.remove_ui()
                    elif choice3=='3':
                        self.updaten_ui()
                    elif choice3=='4':
                        self.updateg_ui()
                    else:
                        print("Bad command")
                elif choice2=='2':
                    self.printEditAss()
                    choice3 = input('>')
                    if choice3 == '1':
                        self.adda_ui()
                    elif choice3 == '5':
                        listass = self._service._assign.listA()
                        for i in listass:
                            print(i)
                    elif choice3 == '2':
                        self.aremove_ui()
                    elif choice3 == '3':
                        self.updatedesc_ui()
                    elif choice3 == '4':
                        self.updatedead_ui()
                    else:
                        print("Bad command")
                else:
                    print("Bad command")
            elif choice =='2':
                self.printGive()
                choice2=input('>')
                if choice2 =='1':
                    self.givestud_ui()
                elif choice2=='2':
                    self.givegroup_ui()
                else:
                    print("Bad command")
            elif choice=='3':
                self.gradestud_ui()
            elif choice=='4':
                self.printstats()
                choice2=input('>>')
                if choice2=='1':
                    listgr = self._service._grades.listG()
                    for i in listgr:
                        print(i)
                elif choice2=='2':
                    self.liststudents_ui()
                elif choice2=='3':
                    self.late_ui()
                elif choice2=='4':
                    self.best_ui()
                else:
                    print('Bad command')
            elif choice=='5':
                    self.undoRedo.undo()
            elif choice =='6':
                try:
                    self.undoRedo.redo()
                except Exception as va:
                    print(va)
            elif choice=='0':
                return
            else:
                print("Bad command")
'''

print('1.For stored repository')
print('2.For Text Repository')
c=input('>')
if c=='1':
    ud = UndoController()
    st=StudentRep(ud)
    ass=AssigmentRep(ud)
    gr=GradeRep(ud)
    s = Service(st,ass,gr,ud)
    s.initS()
    s.initA()
    s.initG()
    ui = UI(s, ud)
    ui.Start()

elif c=='2':
    ud = UndoController()
    st = RepoTextStudents(ud,'students.txt')
    ass = RepoTextAssigments(ud,'assigments.txt')
    gr = RepoTextGrade(ud,'grades.txt')
    s = Service(st, ass, gr, ud)
    ui = UI(s, ud)
    ui.Start()

elif c=='3':
    ud = UndoController()
    st = StudentRep(ud)
    ass = AssigmentRep(ud)
    gr = GradeRep(ud)
    s = Service(st, ass, gr, ud)
    s.initS()
    s.initA()
    s.initG()
    f = open('students.JSON', "w")
    json.dump(s._students.listS(), f)
    f.close()
    f = open('assigments.JSON', "w")
    json.dump(s._assign.listA(), f)
    f.close()
    f = open('grades.JSON', "w")
    json.dump(s._grades.listG(), f)
    f.close()
    st = RepoBinStudents(ud, 'students.JSON')
    ass = RepoBinAssigments(ud, 'assigments.JSON')
    gr = RepoBinGrade(ud, 'grades.JSON')
    s = Service(st, ass, gr, ud)
    ui = UI(s, ud)
    ui.Start()
'''
    






