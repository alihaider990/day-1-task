def find_duplicates(n):
        result = []
        for i in range(len(n)):
            if n[i] not in result:
                result.append(n[i])
            else:
                    return i

num = [1,2,3,4,5,5]
result = find_duplicates(num)
print(result)



























