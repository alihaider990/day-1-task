x = 5     # it is global varaiable

def my_func():
  global x
  y = 9    # it is local variable
  print(y)