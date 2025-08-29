def createCounter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    return increment, decrement


inc, dec = createCounter()
print(inc())  
print(inc())  
print(dec())  