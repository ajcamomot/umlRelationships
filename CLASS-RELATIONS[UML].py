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

class Room:

    def __init__(self, size_sq_ft: int):
        self.size_sq_ft = size_sq_ft


class House:

    def __init__(self):
        self.rooms = [Room(120), Room(250)]

dr_house = House()
print("The house has", len(dr_house.rooms), "rooms.")

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
stem = Department()
Dr_House = Professor("Dr. House")
stem.add_professor(Dr_House)
print("The department has", len(stem.professors), "professors.")
#Association

class Student:

    def __init__(self, name: str):
        self.name = name
        self.courses: list["Course"] = []

    def enroll(self, course: "Course") -> None:
        self.courses.append(course)

class Course:

    def __init__(self, title: str):
        self.title = title
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)
        
Aur = Student("Kendrick Lamar")
StemCourse = Course("YODOTIGOTYOU")
Aur.enroll(StemCourse)
StemCourse.add_student(Aur)
print("The course has", len(StemCourse.students), "students.")
#Dependency

# 6. Dependency
class Printer:
    def __init__(self, name: str):
        self.name = name

    def print_document(self, text: str) -> None:
        print(f"[{self.name}]: {text}")

class ReportGenerator:
    def generate(self, printer: Printer) -> None:
        printer.print_document("Monthly Report")

bound2 = Printer("My Printer")
kanye = ReportGenerator()
kanye.generate(bound2)
#no updated report
