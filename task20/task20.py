class Car:
    def __init__(self, year, brand, model):
        self.year = year
        self.brand = brand
        self.model = model

    def getdetails(self):
        return f"{self.year} {self.brand} {self.model}"

car1 = Car(2008, "mercedes", "c63")
print(car1.getdetails())  