class person:
        def __init__(self, name, age):
          self.age = age
          self.name = age

        def get_age(self):
            return self.age

        def set_age(self, new_age):
                self.age  = new_age

person1 = person("ali", 22)
print(person1.get_age())
person1.set_age(27)
print(person1.get_age())




