'''Student Enrollment system'''
class Person(object):
    '''Student Enrollment System'''
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Aid():
    def __init__(self,scholarship):
        self.scholarship=scholarship

class Student(Person, Aid):
     def __init__(self, name, age, gender, scholarship, rollno):
        Person.__init__(self, name, age, gender)
        Hobby.__init__(self, scholarship)

        self.rollno = rollno

class Department(Student):
    def __init__(self, name, age, gender, scholarship, rollno, school, emailID, major):
        Student.__init__(self, name, age, gender, scholarship, rollno)
        self.school = school
        self.major = major
        self.emailID = emailID

class Semester(Department):
        def __init__(self, name, age, gender, scholarship, rollno, school, emailID, major,semester):
            Department.__init__(self, name, age, gender, scholarship, rollno, school, emailID, major)
            self.grade = semester

class GPA(Semester):
      def __init__(self, name, age, gender, scholarship, rollno, school, emailID, major, semester, GPA):
        Grade.__init__(self, name, age, gender, scholarship, rollno, school, emailID, major, semester)
        self.GPA = GPA

print("***Welcome to XXX Student Enrollment Sytem***\n")
y=input("Did you paid previous semester complete fees? ")
if y in ['y', 'Y', 'yes', 'Yes', 'YES']:
        name = input("Enter name: ")
        age=input("Enter your age? ")
        gender=input("Mention your gender ")
        scholarship=input("Do you have any scholarship? ")
        rollno=input("Please enter roll number: ")
        school=input("Enter your School name: ")
        major=input("What is your major?")
        emailID=input("Enter your email address: ")
        semester=input("Your are in which semester? ")
        GPA=input("Enter your cummulative GPA ")
        print("\nYou will shortly receive an email, regarding your enrollment decision!!! ")
else:
    print("In order to get enroll in next semester pay your previous semester complete fees.")