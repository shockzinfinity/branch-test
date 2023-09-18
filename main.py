def print_hello(num: int):
  """
  Print hello
  """
  for i in range(num):
    if i % 2 == 0:
      print(f'{i}번째 안녕')
    
if __name__ == '__main__':
  print_hello(10)
