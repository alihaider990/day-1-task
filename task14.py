my_list = [1, 3, 4, 6]
targets = [7, 2]

for target in targets:
    for i in range(len(my_list)):
        if my_list[i] >= target:
            print(i)
            break
    else:
        print(len(my_list))