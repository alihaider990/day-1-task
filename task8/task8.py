#def increament(a, b=1):
 #  return a + b

#print(increament(5))






#def factorial(n):
 #   if n == 0 or n == 1:
   #     return 1
    
 #   result = 1
 #   for i in range(2, n + 1):
  #      result = result * i
    
 #   return result


#print(factorial(5))  

#def reverse_string(k):
 #   return k[::-1]
#print(reverse_string("ali haider"))




def second_largest(my_list):
    largest = max(my_list)
    second = 0
    for num in my_list:
        if num > second and num != largest:
           second = num
    return second  


my_list = [34, 61, 23, 67, 89, 21, 70]
result = second_largest(my_list)
print("second largest number is:", result)














    

