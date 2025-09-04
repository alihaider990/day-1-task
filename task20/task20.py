class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):  
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade  

    @staticmethod
    def compare(student1, student2):
        if student1.grade > student2.grade:
            return f"{student1.name} has a higher grade."
        elif student1.grade < student2.grade:
            return f"{student2.name} has a higher grade."
student1 = Student("Ali", 90)
student2 = Student("Hassan", 85)

result = Student.compare(student1, student2)
print(result)  
     