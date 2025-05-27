# University System Display information of
# Classes: Person (parent), and subclasses Student, Lecturer, Staff.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):  
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id} \n")


class Lecturer(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id} \n")
        
        
class Staff(Person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self.staff_id = staff_id

    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id} \n")
        
# Example usage

student = Student("Arthur", 20, "23/U/06534/PS")
lecturer = Lecturer("Dr. Dragule", 45, "LE7890")
staff = Staff("Bob", 35, "STF11223")
person = Person("Alice", 30)

student.display_info()
lecturer.display_info()
staff.display_info()
person.display_info()