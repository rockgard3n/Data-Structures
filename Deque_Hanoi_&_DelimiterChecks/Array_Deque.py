from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__size = 0
    self.__begin = 0
    self.__end = 0
    
  def __str__(self):
    #replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    if self.__size == 0:
      return "[ ]"
    else:
      string = "[ " + str(self.__contents[self.__begin])
      for x in range(1, self.__size):
        string = string + ", " + str(self.__contents[(self.__begin + x)% self.__capacity]) 
      string = string + " ]"
      return string
 
    
  def __len__(self):
    # An implementation that returns the number of
    # items in the deque. This method must run in constant time.
    return self.__size

  def __grow(self):
    # An implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (in order not to limit capacity)
    pastCap = self.__capacity
    pastContent = self.__contents
    self.__capacity = self.__capacity * 2
    self.__contents = [None] * self.__capacity
    for x in range(self.__size):
      self.__contents[x] = pastContent[(x + self.__begin) % pastCap]
    self.__begin = 0
    self.__end = self.__size - 1
    
  def push_front(self, val):
    # An implementation, growing the array before
    # pushing if necessary.
    if self.__size == self.__capacity: 
      self.__grow()
    self.__size = self.__size + 1
    self.__contents[(self.__begin -1)] = val
    self.__begin = (self.__begin -1)
    
  def pop_front(self):
    #Do not reduce the capacity.
    if self.__size > 0:
      pop = self.__contents[self.__begin]
      self.__size = self.__size - 1
      self.__contents[self.__begin] = None
      self.__begin = (1 + self.__begin)
      return pop
    else:
      return
    
  def peek_front(self):
    return self.__contents[self.__begin]
    
  def push_back(self, val):
    #grows the array before pushing if necessary.
    if self.__size < self.__capacity:
      self.__grow()
    self.__size = self.__size + 1
    self.__contents[(self.__end + 1)] = val 
    self.__end = (self.__end + 1)
      
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size > 0:
      pop = self.__contents[self.__end]
      self.__contents[self.__end] = None 
      self.__size = self.__size - 1 
      self.__end = (self.__end -1) 
      return pop
    else:
      return

  def peek_back(self):
    # TODO replace pass with your implementation.
    return self.__contents[self.__end]

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':

