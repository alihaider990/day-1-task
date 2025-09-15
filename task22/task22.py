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





