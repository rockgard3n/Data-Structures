class Fraction:

  def __init__(self, numerator, denominator):
    # use caution here... In most languages, it is not a good idea to
    # raise an exception from a constructor. Python is a bit different
    # and it shouldn't cause a problem here.
    if denominator == 0:
      raise ZeroDivisionError
    self.__n = numerator
    self.__d = denominator
    self.__reduce()

  @staticmethod
  def gcd(n, d):
    while d != 0:
      t = d
      d = n % d
      n = t
    return n

  def __reduce(self):
    if self.__n < 0 and self.__d < 0:
      self.__n = self.__n * -1
      self.__d = self.__d * -1

    divisor = Fraction.gcd(self.__n, self.__d)
    self.__n = self.__n // divisor
    self.__d = self.__d // divisor

  def __add__(self, addend):
    num = self.__n * addend.__d + self.__d * addend.__n
    den = self.__d * addend.__d
    return Fraction(num, den)

  def __sub__(self, subtrahend):
    num = self.__n * subtrahend.__d - self.__d * subtrahend.__n
    den = self.__d * subtrahend.__d
    return Fraction(num, den)

  def __mul__(self, multiplicand):
    num = self.__n * multiplicand.__n
    den = self.__d * multiplicand.__d
    return Fraction(num, den)

  def __truediv__(self, divisor):
    if divisor.__n == 0:
      raise ZeroDivisionError
    num = self.__n * divisor.__d
    den = self.__d * divisor.__n
    return Fraction(num, den)

  def __lt__(self, other):
    #TODO replace pass with your implementation,
    #returning True if self is less than other and
    #False otherwise.
    if self.__sub__(other).__n / self.__sub__(other).__d < 0:
      return True
    else:
      return False

  def __gt__(self, other):
    #TODO replace pass with your implementation,
    #returning True if self is greater than other and
    #False otherwise.
    if self.__sub__(other).__n / self.__sub__(other).__d > 0:
      return True
    else:
      return False

  def __eq__(self, other):
    #TODO replace pass with your implementation,
    #returning True if self equal to other and
    #False otherwise. Note that fractions are
    #stored in reduced form.
    if self.__n == other.__n and self.__d == other.__d:
      return True
    else:
      return False

  def to_float(self):
    #this is safe because we don't allow a
    #zero denominator
    return self.__n / self.__d

  def __str__(self):
    return str(self.__n) + '/' + str(self.__d)

  # the __repr__ method is similar to __str__, but is called
  # when Python wants to display these objects in a container like
  # a Python list.
  def __repr__(self):
    return str(self)

if __name__ == '__main__':
  #TODO create a bunch of fraction objects and store them in an array.
  #Then insert each item from the array into a balanced BST.
  #Then get the in-order array representation of the BST using
  #the new to_list() method, which you must implement.
  #print the original and in-order traversal arrays to show that
  #the fractions have been sorted.
  from Binary_Search_Tree import Binary_Search_Tree
  fraction_tree = Binary_Search_Tree()
  fraction_list = []
  
  frac1 = Fraction(1,2)
  frac2 = Fraction(2,5)
  frac3 = Fraction(5,6)
  frac4 = Fraction(-5,3)
  frac5 = Fraction(4,-2)
  frac6 = Fraction(10, 12)
  frac7 = Fraction(3,8)
  frac8 = Fraction(4,9)
  frac9 = Fraction(10,4)
  frac10 = Fraction(74,98)
  
  fraction_list.append(frac1)
  fraction_list.append(frac2)
  fraction_list.append(frac3)
  fraction_list.append(frac4)
  fraction_list.append(frac5)
  fraction_list.append(frac6)
  fraction_list.append(frac7)
  fraction_list.append(frac8)
  fraction_list.append(frac9)
  fraction_list.append(frac10)
  print(fraction_list)
  
  for x in fraction_list:
    fraction_tree.insert_element(x)
  
  print(fraction_tree.to_list())
  
  