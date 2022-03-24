class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      self.val = val
      self.next = None
      self.prev = None

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class

    self._header = Linked_List.__Node(None)
    self._trailer = Linked_List.__Node(None)
    self._size = 0
    self._header.next = self._trailer 
    self._trailer.prev = self._header

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.

    return self._size

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this 
    # is the only way to add items at the tail position.
    
    app = Linked_List.__Node(val)
    #connects new node with previous last-position node
    if self._size == 0:
      self._header.next = app
      app.prev = self._header     
    else:
      selection = self._trailer.prev
      selection.next = app
      app.prev = selection
      
    
    #completes 2 way link by connecting append and trialer
    self._trailer.prev = app
    app.next = self._trailer      
      

    
    #increase size by 1
    self._size = self._size + 1
      

  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the 
    # specified index. If the index is not a valid 
    # position within the list, raise an IndexError 
    # exception. This method cannot be used to add an 
    # item at the tail position.

    #special case catch using if statements
    if index < 0 or index >= self._size:
      raise IndexError
    
    #creates node variables we will use to manipulate list
    insert = Linked_List.__Node(val)
    selection = self._header
    
    #iterates through list until index
    for x in range(index):
      selection = selection.next
    
    #inserts the new node without losing any other nodes to garbage collector
    post_insert = selection.next
    post_insert.prev = insert 
    insert.next = post_insert
    selection.next = insert
    insert.prev = selection
    
    #increase size by 1
    self._size = self._size+1
    
    

  def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored 
    # in the node at the specified index. If the index 
    # is invalid, raise an IndexError exception.
    
    #special case catch
    if index < 0 or index >= self._size:
      raise IndexError
    
    #creates node variable to manipulate list
    selection = self._header
    
    #iterates through lest until arrives at desired position
    for x in range(index):
      selection = selection.next
    
    #holds return value
    retrn = selection.next 
    
    #removes desired position and decreases size by 1
    selection.next = selection.next.next 
    selection.next.prev = selection
    self._size = self._size - 1 
    
    return retrn.val 
    

  def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node 
    # at the specified index, but do not unlink it from 
    # the list. If the specified index is invalid, raise 
    # an IndexError exception.

    #special case catch 
    if index < 0 or index >= self._size:
      raise IndexError
    
    #creates node variable to manipulate list
    selection = self._header
    
    #iterates to desired position 
    for x in range(index+1):
      selection = selection.next
    
    return selection.val
    

  def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    
    #special case catch 
    if self._size == 0 or self._size == 1:
      return
    
    #finds first position
    selection = self._header.next 
    
    #rotates conceptual indices left
    selection.next.prev = self._header
    self._trailer.prev.next = selection
    selection.prev = self._trailer.prev
    self._trailer.prev = selection
    self._header.next = selection.next
    selection.next = self._trailer
    #selection.prev.next = selection
    
    
  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.

    #special case catch
    if self._size == 0:
      return "[ ]"
    
    #creates and returns string object
    else:
      string = "[ "
      selection = self._header.next
      string = string + str(selection.val)
      for x in range(1,self._size):
        selection = selection.next 
        string = string + "," + " " + str(selection.val)
      string = string + " ]"
      
      return string
      

  def __iter__(self):
    # initialize a new attribute for walking through your list
    # statement. do not modify the return statement.
    self.position = self._header.next
   
    
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.

    if self.position is self._trailer:
      raise StopIteration
    
    rtrn = self.position
    self.position = self.position.next
    
    return rtrn.val
    

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  
  test = Linked_List()
  
  print("Empty List Check")
  #Empty List Check: Does each function respond correctly to empty lists
  ##Insert
  try:
    #should not be able to add to head of empty list
    test.insert_element_at(5,0)
  except IndexError:
    print("Correctly caught attempt to insert in empty list")
  print(str(test))
  ##Remove
  print(len(test))
  try:
    #should return error 
    test.remove_element_at(0)
  except IndexError:
    print("Correctly caught attempt to remove from empty list")
  print(str(test))
  ##Get Element
  try:
    #should return error
    test.get_element_at(0)
  except IndexError:
    print("Correctly caught attempt to get element from empty list")
  print(str(test))
  ##Rotate
  #should return without error or effect
  test.rotate_left()
  print(str(test))
  print()
  
  print("Append Check")
  #Append Check: for all lists adds element at new tail, increments size by 1
  ##empty

  test.append_element(5)
  print(str(test))
  print(len(test))
  ##list size one

  test.append_element(1)
  print(str(test))
  print(len(test))
  ##Lists of size greater than 1

  test.append_element(4)
  print(str(test))
  print(len(test))
  
  test.append_element(2)
  print(str(test))
  print(len(test))
  
  test.append_element(-1)
  print(str(test))
  print(len(test))
  print()
  
  print("Insert Check")
  #Insert Check (valid index): +size by 1, modify list structure correctly

  test.insert_element_at(0, 3)
  print(str(test))
  print(len(test))    
  #insert at position 0 check
  test.insert_element_at(-3,0)
  print(str(test))
  print(len(test))

  #Insert Check (invalid index): should leave list unchanged 
  try:
    pass
    test.insert_element_at(-1,-1)
    test.insert_element_at(2,5)
  except IndexError:
    print("Correctly caught attempt to add element to invalid index")
    print(str(test))
    print(len(test))    
  print()
  
  print("Remove Check")
  #Remove Check (valid index): -1 size by 1, modify list structure correctly
  #also checks to ensure remove element is returning value
  try:
    print(str(test))
    print("element removed was " + str(test.remove_element_at(3)))
    print(str(test))
    test.remove_element_at(0)
    print("element removed was " + str(test.remove_element_at(0)))
    print(str(test))
    print(len(test))       
  except IndexError:
    print("Error: Code Malfunction")
  
  #Remove Check (invalid index): should leave list unchanged
  try:
    test.remove_element_at(-1)
  except IndexError:
    print("Correctly caught attempt to remove element at invalid negative index")
  try:
    test.remove_element_at(6)
  except IndexError:
    print("Correctly caught attempt to remove element at invalid positive index")
  print()
  
  #Loop Check: Does loop visit every value
  print("Loop Check")
  for val in test:
      print(val)
  print()
  looptest = Linked_List()
  for val in looptest:
    print(val)
  print()
  
  print("Get_Element Check") 
  #Get Element Check: Does the function pull the correct value
  ##Valid Index
  try:
    print(str(test))
    print("The element found was "+str(test.get_element_at(3)))
    print("The element found was "+str(test.get_element_at(4)))
    print("The element found was "+str(test.get_element_at(0)))
    print(str(test))
    print(len(test))
  except IndexError:
    print("Error: Code Malfunction")
  ##Invalid Index
  try:
    test.get_element_at(-1)
  except IndexError:
    print("Correctly caught attempt to find element at invalid negative index")
  try:
    test.get_element_at(5)
  except IndexError:
    print("Correctly caught attempt to find element at invalid positive index")
  print()
  
  print("Rotate Check")
  #Rotate Check: Does the function correctly rotate our list
  test.rotate_left()
  print(str(test))
  print("Rotation of size 1 list")
  test1 = Linked_List()
  test1.append_element(3)
  test1.rotate_left()
  print(str(test1))
  print("Rotation of size 2 list")
  test1.append_element(0)
  print(str(test1))
  test1.rotate_left()
  print(str(test1))

