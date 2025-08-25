#numbers = [1, 2, 3, 4, 5]

#def is_even(x):
 #   return x % 2 == 0

#def double(x):
  #  return x * 2

#doubled_even = map(double, filter(is_even, numbers))

#for num in doubled_even:
  #  print(num)


#names = []
#marks = []

#for i in range(5):
  #  name = input("Enter student name: ")
#    mark = int(input("Enter marks: "))
  #  names.append(name)
 #   marks.append(mark)

#for i in range(5):
   # print(names[i], "got", marks[i], "marks")

#max_index = marks.index(max(marks))
#print(names[max_index], "got highiest marks")































def  first_unique_char(k):
    for i in range(len(k)):
        if k.count(k[i]) == 1:
            return i
        return -1
        k = "wwarzone"
        print(first_unique_char(k))

