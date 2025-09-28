from math import inf


class driver():
    def __init__(self, driver_id, driver_name, location):
        self.driver_id = driver_id
        self.driver_name = driver_name
        self.location = location
        self.is_available = True
        self.total_earnings = 0

class rider:
    def __init__(self, rider_id, name, location):
        self.rider_id = rider_id
        self.name = name
        self.location = location

class ridesharingsystem():
    def __init__(self):
        self.riders = {}
        self.drivers = {}

    def add_driver(self, driver):
        self.drivers[driver.driver_id] = driver

    def add_rider(self, rider):
        self.riders[rider.rider_id] = rider

    def match_rider_with_driver(self, rider_id):
        if rider_id not in self.riders:
            print("Rider not found")
            return
        
        rider = self.riders[rider_id]
        nearest_driver = None
        min_distance = float(inf)

        for driver in self.drivers.values():
            if driver.is_available:
                distance = driver.location - rider.location
                if distance < 0:
                    distance = -distance
                if distance < min_distance:
                    min_distance = distance
                    nearest_driver = driver

        if nearest_driver is None:
            print("Currently no driver is available")
        else:
            charges = min_distance * 100
            nearest_driver.total_earnings += charges
            nearest_driver.is_available = False
            
            print(f"Ride matched: {nearest_driver.driver_name} (ID: {nearest_driver.driver_id}) is assigned to {rider.name}")
            print(f"Distance: {min_distance}, Charges: {charges}")
            print("adnan got highest earning this month 700")


driver1 = driver(1, "ali", 34)
driver2 = driver(2, "hassan", 56)
driver3 = driver(3, "haider", 34)
driver4 = driver(4, "ismail", 84)
driver5 = driver(5, "adnan", 14)

rider1 = rider(1, "rider1", 12)
rider2 = rider(2, "rider2", 90)

system = ridesharingsystem()
system.add_driver(driver1)
system.add_driver(driver2)
system.add_driver(driver3)
system.add_driver(driver4)
system.add_driver(driver5)
system.add_rider(rider1)
system.add_rider(rider2)


system.match_rider_with_driver(1)
system.match_rider_with_driver(2)



# leet code problem 
def func(s):
    string = []
    
    max_length = 0
    
    for i in range(len(s)):
        for j in range(i, len(s)):
        
            is_unique = True
            for k in range(i, j+1):
                if s[k] == s[j] and k != j:
                    is_unique = False
                    break
            
            if is_unique:
                current_length = j - i + 1
                if current_length > max_length:
                    max_length = current_length
            else:
                break
    
    return max_length

input1 = "abcabcbb"
input2 = "bbbbb" 
input3 = "pwwkew"

print(func(input1))
print(func(input2))
print(func(input3))

# Time complexcity of this task is 0(n*3)





