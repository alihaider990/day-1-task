#def add_numbers(a, b):
  #  return a + b


#result = add_numbers(5, 3)
#print("Sum:", result)



#def find_max(numbers):
  #  return max(numbers)


#nums = [5, 1, 3, 9, 78, 7]
#maximum = find_max(nums)
#print("Maximum number:", maximum)


def sum_of_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total


nums = [4, 7, 8, 9, 6, 1, 5]
even_sum = sum_of_even(nums)
print("Sum of even numbers:", even_sum)



