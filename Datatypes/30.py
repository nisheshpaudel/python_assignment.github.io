d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present.')
  else:
      print('Key is not present.')
is_key_present(3)
is_key_present(7)