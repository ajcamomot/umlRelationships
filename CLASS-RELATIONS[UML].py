#Inheritance

class Animal:

    def __init__(self, name: str):
        self.name = name

    def make_sound(self) -> None:
        pass


class Dpg(Animal):

    def bark(self) -> None:
        print("Woof!")


#Composition

class room:

    def __init__(self, size_sq_ft: int):
        self.size_sq_ft = size_sq_ft


class House:

    def __init__(self):
        self.rooms = [room(120), room(250)]


#Realization


class Drivable():

    def drive(self) -> None:
        pass


class Car(Drivable):

    def drive(self) -> None:
        print("Driving")


#Aggregation

class Professor:

    def __init__(self, name: str):
        self.name = name


class Deparrtment:

    def __init__(self):
        self.professors: list[Professor] = []

    def add_professor(self, professor: Professor) -> None:

        self.professors.append(professor)

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

#Dependency

class Printer:

    def print_document(self, text: str) -> None:
        print(text)


class ReportGenerator:

    def generate(self, printer: Printer) -> None:
        printer.print_document("Monthly Report")