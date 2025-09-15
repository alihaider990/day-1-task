class Shape:
    def area(self):
        
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        
        return self.width * self.height


rect = Rectangle(5, 3)
print(rect.area())  



#leet code task 1

def reverse_integer(n):
    s = str(n)
    result = []
    for i in range(len(s) - 1, -1, -1):  #time complexity is o(k) becasue we are iterating through the string.
        result.append(s[i])
    return int(''.join(result))

print(reverse_integer(123))                  



#leet code task 2

def find_duplicates(n):
    seen = set()
    for i in range(len(n)):  #time complexcity is o(n) because we are iterating through the list. 
        if n[i] not in seen:
            seen.add(n[i])
        else:
            return i

num = [1,2,3,4,5,5]
result = find_duplicates(num)
print(result)

