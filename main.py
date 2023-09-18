def print_hello(num: int):
  """
  Print hello
  """
  for i in range(num):
    print(f'{i + 1}번째 안녕')
    
if __name__ == '__main__':
  print_hello(10)