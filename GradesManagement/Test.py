import unittest
from student import *
from studentrep import *
from assigment import *
from assigmentrep import *
from service import *
from UndoController import *

class Teststudent(unittest.TestCase):
    def testStud(self):
        s=Student(1,'Fabian Catalin',913)
        self.assertEqual(s.SId,1)
        self.assertEqual(s.Name,'Fabian Catalin')
        self.assertEqual(s.Group,913)
    def teststudeexcep(self):
        with self.assertRaises(NameError):
            Student(1,'F',913)
        with self.assertRaises(GroupError):
            Student(1,'Fabian ',100)
        with self.assertRaises(NoID_S):
            Student(None,'Fabian ',911)
class Testassigment(unittest.TestCase):
    def testAssigment(self):
        a=Assigment(101,'Exercise 12',12)
        self.assertEqual(101,a.AId)
        self.assertEqual(a.Desc,'Exercise 12')
        self.assertEqual(a.Dead,12)
    def testassexcept(self):
        with self.assertRaises(NoID_A):
            Assigment(None, 'Exercise 12 ', 12)
        with self.assertRaises(LengthError):
            Assigment(101,'e', 12)


class Teststudentrep(unittest.TestCase):
    def test_add(self):
        s1 = Student(1, 'Fabian Catalin', 913)
        s2 = Student(2, 'Dobra Darius', 913)
        s3 = Student(3, 'Fodor Andrei', 913)
        st=StudentRep(ud)
        st.addS(s1)
        self.assertEqual(1,len(st._studentRep))
        st.addS(s2)
        st.addS(s3)
        self.assertEqual(3,len(st._studentRep))
        with self.assertRaises(DuplicateId):
            st.addS(s1)
    def test_remove(self):
        s1 = Student(1, 'Fabian Catalin', 913)
        s2 = Student(2, 'Dobra Darius', 913)
        s3 = Student(3, 'Fodor Andrei', 913)
        st = StudentRep(ud)
        st.addS(s1)
        st.addS(s2)
        st.addS(s3)
        st.removeS(1)
        self.assertEqual(2,len(st._studentRep))
        with self.assertRaises(NoID_S):
            st.removeS(12)
    def test_updatename(self):
        s1 = Student(1, 'Fabian Catalin', 913)
        st = StudentRep(ud)
        st.addS(s1)
        st.updaten(1,'Daria')
        self.assertEqual(s1.Name,'Daria')
        with self.assertRaises(NoID_S):
            st.updaten(11,'Anda')
    def test_updategroup(self):
        s1 = Student(1, 'Fabian Catalin', 913)
        st = StudentRep(ud)
        st.addS(s1)
        st.updateg(1,914)
        self.assertEqual(s1._group,914)
class Testassigmentrep(unittest.TestCase):
    def test_add(self):
        a1 = Assigment(101, 'Exercise 1', 3)
        a2 = Assigment(102, 'Exercise 2', 3)
        a3 = Assigment(103, 'Exercise 3', 3)
        asg=AssigmentRep(ud)
        asg.addA(a1)
        self.assertEqual(1,len(asg._assigmentRep))
        asg.addA(a2)
        asg.addA(a3)
        self.assertEqual(3,len(asg._assigmentRep))
        with self.assertRaises(DuplicateId):
            asg.addA(a1)
    def test_remove(self):
        a1 = Assigment(101, 'Exercise 1', 3)
        a2 = Assigment(102, 'Exercise 2', 3)
        a3 = Assigment(103, 'Exercise 3', 3)
        asg = AssigmentRep(ud)
        asg.addA(a1)
        asg.addA(a2)
        asg.addA(a3)
        asg.removeA(101)
        self.assertEqual(2,len(asg._assigmentRep))
        with self.assertRaises(NoID_A):
            asg.removeA(105)
    def test_updatedesc(self):
        a1 = Assigment(101, 'Exercise 1', 3)
        asg = AssigmentRep(ud)
        asg.addA(a1)
        asg.updatedesc(101,'Exercise 2')
        self.assertEqual(a1.Desc,'Exercise 2')
        with self.assertRaises(NoID_A):
            asg.updatedesc(111,'Exercise 2')
    def test_updatedead(self):
        a1 = Assigment(101, 'Exercise 1', 3)
        asg = AssigmentRep(ud)
        asg.addA(a1)
        asg.updatedead(101, 4)
        self.assertEqual(a1.Dead, 4)

if __name__ == '__main__':
    unittest.main()

ud=UndoController()
