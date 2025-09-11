def reverse_integer(n):
    reversed_str = ""
    for char in str(n):
        reversed_str = char + reversed_str
    return int(reversed_str)

num = 123
result = reverse_integer(num)
print(result)












