my_list = [12, 31, 34, 34, 64, 65, 78, 87, 90]  
target = 90

left = 0
right = len(my_list) - 1

found = False
while left <= right:
    middle = (left + right) // 2
    if my_list[middle] == target:
        print(middle)
        found = True
        break
    elif my_list[middle] < target:
        left = middle + 1
    else:
        right = middle - 1

if not found:
    print(-1)
