class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

class Student(Person):  
    def __init__(self, name, age, grade):
        super().__init__(name, age)  
        self._grade = grade          

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value

    
    def get_age(self):
        return f"{self.name} is {self.age} years old and in grade {self.grade}"


student1 = Student("Ali", 22, "9")
print(student1.get_age())  





