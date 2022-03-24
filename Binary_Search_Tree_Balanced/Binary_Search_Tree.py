class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      self._left = None
      self._right = None
      self._height = 1
      self._balance_val = 0

  def __init__(self):
    self.__root = None
    self._size = 0
    
  def _balance(self, NodeRef):
    if NodeRef is not None:
      if NodeRef._balance_val == 2:
        if NodeRef._right._balance_val > 0:
          NodeRef = self._left_rotation(NodeRef)
        else:
          NodeRef._right = self._right_rotation(NodeRef._right)
          NodeRef = self._left_rotation(NodeRef)
      elif NodeRef._balance_val == -2:
        if NodeRef._left._balance_val < 0:
          NodeRef = self._right_rotation(NodeRef)
        else:
          NodeRef._left = self._left_rotation(NodeRef._left)
          NodeRef = self._right_rotation(NodeRef)
      else:
        return NodeRef
    else:
      return NodeRef
    self.update_height(NodeRef)
    return NodeRef
  
  def _right_rotation(self, NodeRef):
    selection = NodeRef._left
    NodeRef._left = selection._right
    selection._right = NodeRef
    self.update_height(NodeRef)
    self.update_height(selection)
    return selection
  
  def _left_rotation(self, NodeRef): 
    selection = NodeRef._right
    NodeRef._right = selection._left
    selection._left = NodeRef
    self.update_height(NodeRef)
    self.update_height(selection)
    return selection

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = self._recursive_insert(value, self.__root)
    #self.__root = self._balance(self.__root)
    self._size = self.__root._height
    
  def _recursive_insert(self, value, nodeRef):
    if nodeRef is None:
      nodeRef = self.__BST_Node(value)
    
    elif value == nodeRef.value:
      return nodeRef

    else:
      if value > nodeRef.value:
        nodeRef._right = self._recursive_insert(value, nodeRef._right)
      elif value < nodeRef.value:
        nodeRef._left = self._recursive_insert(value, nodeRef._left)
        
    #update height function needs to be recursive function because it also updates the balance value of the node    
    self.update_height(nodeRef)
    return self._balance(nodeRef)

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
      self.__root = self._recursive_remove(value, self.__root)
      #self.update_height(self.__root)
      if self.__root != None:
        self._size = self.__root._height
   
  def _recursive_remove(self, value, nodeRef):
    if nodeRef is None: 
      return
    else:
      if value == nodeRef.value:
            if nodeRef._left != None and nodeRef._right != None:
              nodeRef.value = self._min_finder(nodeRef._right)
              nodeRef._right = self._recursive_remove(nodeRef.value, nodeRef._right)  
            elif nodeRef._left == None:
              nodeRef = nodeRef._right    
            else:
              nodeRef = nodeRef._left   
      elif value > nodeRef.value:
            nodeRef._right = self._recursive_remove(value, nodeRef._right)
      else: #value < nodeRef.value:
            nodeRef._left = self._recursive_remove(value, nodeRef._left)
    
    #update height function needs to be recursive function because it also updates the balance value of the node (this is a change from project 4 code)
    self.update_height(nodeRef)
    return self._balance(nodeRef)

  def _min_finder(self, nodeRef):
    while nodeRef._left is not None:
      nodeRef = nodeRef._left
    return nodeRef.value
  
  def update_height(self, nodeRef):
    if nodeRef is None:
      return
    else:
      if nodeRef._right is None:
        right_height = 0
      else:
        right_height = nodeRef._right._height
      if nodeRef._left is None:
        left_height = 0
      else:
        left_height = nodeRef._left._height
      if left_height <= right_height:
        nodeRef._height = right_height + 1
      if left_height >=  right_height:
        nodeRef._height = left_height + 1
      self._height = nodeRef._height 
      nodeRef._balance_val = right_height - left_height
      self._balance_val = nodeRef._balance_val
      #print(self._balance_val)

     
  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.get_height() == 0:
      string = "[ ]"
    else:
      string = "[ " + self._recursive_in_order(self.__root)[:-2] + " ]"
    return string
    
  
  def _recursive_in_order(self, nodeRef):
    if nodeRef == None:
      return ""   
    
    else:
      return self._recursive_in_order(nodeRef._left) + str(nodeRef.value) + ", " + self._recursive_in_order(nodeRef._right) 



  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.get_height() == 0:
      string = "[ ]"
    else:
      string = "[ " + self._recursive_pre_order(self.__root)[:-2] + " ]"
    return string
    
  
  def _recursive_pre_order(self, nodeRef):
    if nodeRef == None:
      return ""   
    
    else:
      return str(nodeRef.value) + ", " + self._recursive_pre_order(nodeRef._left) + self._recursive_pre_order(nodeRef._right)   


  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.get_height() == 0:
      string = "[ ]"
    else:
      string = "[ " + self._recursive_post_order(self.__root)[:-2] + " ]"
    return string
    
  
  def _recursive_post_order(self, nodeRef):
    if nodeRef == None:
      return ""   
    
    else:
      return  self._recursive_post_order(nodeRef._left) + self._recursive_post_order(nodeRef._right) + str(nodeRef.value) + ", " 


  def to_list(self):
    lists = []
    if self.get_height() == 0:
      return lists
    else:
      lists = self._recursive_to_list(self.__root, lists)
    return lists
    
  
  def _recursive_to_list(self, nodeRef, lists):
    if nodeRef == None:
      return
    
    else:
      self._recursive_to_list(nodeRef._left, lists)
      lists.append(nodeRef.value) 
      self._recursive_to_list(nodeRef._right, lists)
      return lists
    
    
  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root is not None:
      return self._size
    else:
      return 0

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.
  
