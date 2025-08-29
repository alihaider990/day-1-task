def createCounter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter


counter = createCounter()
print(counter())  
print(counter())  
print(counter())  