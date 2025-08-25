my_list = [65,30,20,90]
target = 50

for i in range(len(my_list)):
    for j in range(i + 1,len(my_list)):
        if my_list[i] + my_list[j] == target:
         print([i,j])
