class Person(object):
    # constructor to create an object
    countt = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.increaseCount()

    def increaseCount(self):
        self.__class__.countt += 1
        # return self.count


class Student(Person):
    # constructor to create an object

    def __init__(self, name, age, rollno):
        Person.__init__(self, name, age)
        self.rollno = rollno

    def details(self):
        return "%s is %s year old and %s is his rollnumber" % (self.name, int(self.age), int(self.rollno))


class TransferStudent(Student):
    def __init__(self, name, age, rollno, grade):
        Student.__init__(self, name, age, rollno)
        self.grade = grade

    def detail(self):
        return("%s is %s years old and %s is his rollno. He got %s grade." % (self.name, int(self.age), int(self.rollno), self.grade))

StudenT = Student("Mahmood", 24, 12313)
# StudenT.countt()
print("Number of students are", StudenT.__class__.countt)
StudenTT = Student("uzair", 44, 313)
# StudenTT.countt()

print(StudenT.details())

print(StudenTT.details())
print("Number of students are", StudenTT.__class__.countt)

student1=TransferStudent("Roo", 34, 123, "A")
print(student1.detail())
print("Number of students are", student1.__class__.countt)