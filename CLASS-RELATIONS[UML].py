#Inheritance

class Animal:

    def __init__(self, name: str):
        self.name = name

    def make_sound(self) -> None:
        pass

class Dog(Animal):

    def bark(self) -> None:
        print("Woof!")
dog = Dog("Virgil Kendritz R Alonso")
dog.bark()

#Composition

class room:

    def __init__(self, size_sq_ft: int):
        self.size_sq_ft = size_sq_ft


class House:

    def __init__(self):
        self.rooms = [room(120), room(250)]

dr_house = House()

#Realization


class Drivable():

    def drive(self) -> None:
        pass


class Car(Drivable):

    def drive(self) -> None:
        print("Driving")
car = Car()
car.drive()

#Aggregation

class Professor:

    def __init__(self, name: str):
        self.name = name


class Department:

    def __init__(self):
        self.professors: list[Professor] = []

    def add_professor(self, professor: Professor) -> None:

        self.professors.append(professor)
Stem = Department()
Dr_House = Stem("Dr. House")
Stem.add_professor(Dr_House)

#Association

class student:

    def __init__(self, name: str):
        self.name = name
        self.courses: list["Course"] = []

    def enroll(self, course: "Course") -> None:
        self.courses.append(course)

class Course:

    def __init__(self, title: str):
        self.title = title
        self.students: list[student] = []

    def add_student(self, student: student) -> None:
        self.students.append(student)
        
Aur = student("Kendrick Lamar")
StemCourse = Course("YODOTIGOTYOU")
Aur.enroll(StemCourse)
StemCourse.Course.add_student(Aur)

#Dependency

class Printer:

    def print_document(self, text: str) -> None:
        print(text)


class ReportGenerator:

    def generate(self, printer: Printer) -> None:
        printer.print_document("Monthly Report")

BOUND2 = Printer("My Printer")
Kanye = ReportGenerator()
Kanye.generate.(BOUND2)
