def multiplyBy(n):
    def multiplier(x):
        return x * n
    return multiplier


double = multiplyBy(2)
triple = multiplyBy(3)

print(double(5))  
print(triple(5)) 