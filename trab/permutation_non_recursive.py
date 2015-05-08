import math

class permutations:
  def __init__(self, number):
    self.numbers = split(number)

    self.used = {}
    self.used_in_columns = []
    for number in self.numbers:
      self.used_in_columns.append({})
    self.i = 0
    self.current = []
    self.total_permutations = math.factorial(len(self.numbers))

  def __iter__(self):
    return self

  def next(self):
    if self.i == self.total_permutations:
      raise StopIteration()

    while not self.number_can_be_pushed():
      if len(self.current) < len(self.numbers):
        self.used_in_columns[len(self.current)] = {}
      removed = self.current.pop()
      self.used[removed] = False

    while len(self.current) != len(self.numbers):
      for i,num in enumerate(self.numbers):
        column = self.used_in_columns[len(self.current)]
        if not self.used.get(num) and not column.get(num):
          self.current.append(num)
          self.used[num] = True
          column[num] = True
          break

    self.i += 1
    number = join(self.current)
    #if number == 231:
    #  return self.next()
    return number

  def number_can_be_pushed(self):
    if len(self.current) == len(self.numbers):
      return False
    else:
      for num in self.numbers:
        if not self.used_in_columns[len(self.current)].get(num) and not self.used.get(num):
          return True
      return False

def split(number):
  digits = []
  while number != 0:
    digits.insert(0, number % 10)
    number = number / 10
  return digits

def join(digits):
  number = 0
  for digit in digits:
    number *= 10
    number += digit
  return number


#for perm in permutations(123):
#  print perm
