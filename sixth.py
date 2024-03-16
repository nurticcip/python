class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Student(Person):
    def __init__(self, first_name, last_name, student_id):
        super().__init__(first_name, last_name)
        self.student_id = student_id

    def info(self):
        return f"Student: {self.full_name()}, ID: {self.student_id}"
    
person = Person("Нуртилек", "Абибиллаев")
student = Student("Нуртилек", "Абибиллаев", "24364765")

print(person.full_name())  
print(student.info())     