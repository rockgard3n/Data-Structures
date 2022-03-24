import unittest
from Deque_Generator import get_deque, LL_DEQUE_TYPE, ARR_DEQUE_TYPE
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    # Run your tests with each deque type to ensure that
    # they behave identically.
    self.__deque = get_deque(LL_DEQUE_TYPE)
    self.__stack = Stack()
    self.__queue = Queue()
  #Empty Tests  
  def test_empty_deque(self):
    self.assertEqual('[ ]', str(self.__deque), 'Empty deque should print as "[ ]"')
  
  def test_empty_stack(self):
    self.assertEqual('[ ]', str(self.__stack), 'Empty stack should print as "[ ]"')
  
  def test_empty_queue(self):
    self.assertEqual('[ ]', str(self.__queue), 'Empty queue should print as "[ ]"')
  
  #Deque Tests
  ##push tests starting with empty deque up to two, tests to make sure push 
  ##functions create proper deques with proper string format and len
  def test_push_front_empty_deque(self):
    self.__deque.push_front('Victory')
    self.assertEqual('[ Victory ]', str(self.__deque))
    self.assertEqual(1, len(self.__deque))
  
  def test_push_front_empty_deque_length(self):
    self.__deque.push_front('Victory')
    self.assertEqual(1, len(self.__deque))  
  
  def test_push_front_single_deque(self):
    self.__deque.push_front('Victory')
    self.__deque.push_front('have')
    self.assertEqual('[ have, Victory ]', str(self.__deque)) 
  
  def test_push_front_single_deque_length(self):
    self.__deque.push_front('Victory')
    self.__deque.push_front('have')
    self.assertEqual(2, len(self.__deque))  
  
  def test_push_front_double_deque(self):
    self.__deque.push_front('Victory')
    self.__deque.push_front('have')
    self.__deque.push_front('we')
    self.assertEqual('[ we, have, Victory ]', str(self.__deque))
    self.assertEqual(3, len(self.__deque))
  
  def test_push_front_double_deque_length(self):
    self.__deque.push_front('Victory')
    self.__deque.push_front('have')
    self.__deque.push_front('we')
    self.assertEqual(3, len(self.__deque))  

  ##pop front tests starting with empty deque working up to two, tests make 
  ##sure pop functions create proper deques with proper string format and len
  def test_pop_front_empty_deque(self):
    with self.assertRaises(IndexError):
      pop = self.__deque.pop_front()
      self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_single_deque_string(self):
    self.__deque.push_front('Liam')
    pop = self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))
  
  def test_pop_front_single_deque_popvalue(self):
    self.__deque.push_front('Liam')
    pop = self.__deque.pop_front()
    self.assertEqual('Liam', pop)

  def test_pop_front_single_deque_length(self):
    self.__deque.push_front('Liam')
    pop = self.__deque.pop_front()
    self.assertEqual(0, len(self.__deque)) 
  
  def test_pop_front_double_deque_string(self):
    self.__deque.push_front('Liam')
    self.__deque.push_front('Coolguy')
    pop = self.__deque.pop_front()
    self.assertEqual('[ Liam ]', str(self.__deque))
  
  def test_pop_front_double_deque_popvalue(self):
    self.__deque.push_front('Liam')
    self.__deque.push_front('Coolguy')
    pop = self.__deque.pop_front()
    self.assertEqual('Coolguy', pop)  
  
  def test_pop_front_double_deque_length(self):
    self.__deque.push_front('Liam')
    self.__deque.push_front('Coolguy')
    pop = self.__deque.pop_front()
    self.assertEqual(1, len(self.__deque))   
  
  ##peek front tests starting with empty deque working up to deque with 2 
  ##entries. Test makes sure peek function working correctly without affecting
  ##entries in deque
  def test_peek_front_empty_deque(self):
    with self.assertRaises(IndexError):
      peek = self.__deque.peek_front()
      self.assertEqual('[ ]', str(self.__deque))
    
  def test_peek_front_single_deque_string(self):
    self.__deque.push_front('Liam')
    peek = self.__deque.peek_front()
    self.assertEqual('[ Liam ]', str(self.__deque))
  
  def test_peek_front_single_deque_peekvalue(self):
    self.__deque.push_front('Liam')
    peek = self.__deque.peek_front()
    self.assertEqual('Liam', peek)

  def test_peek_front_single_deque_length(self):
    self.__deque.push_front('Liam')
    peek = self.__deque.peek_front()
    self.assertEqual(1, len(self.__deque))
  
  def test_peek_front_double_deque_string(self):
    self.__deque.push_front('Victory')
    self.__deque.push_front('have')
    peek = self.__deque.peek_front()
    self.assertEqual('[ have, Victory ]', str(self.__deque)) 
  
  def test_peek_front_double_deque(self):
    self.__deque.push_front('Liam')
    self.__deque.push_front('Coolguy')
    peek = self.__deque.peek_front()
    self.assertEqual('Coolguy', peek) 
  
  def test_peek_front_double_deque(self):
    self.__deque.push_front('Liam')
    self.__deque.push_front('Coolguy')
    self.assertEqual(2, len(self.__deque))
  
  ##push back tests starting with empty deque working up to deque with 2 
  ##entries. Test ensures push back function creating correct deque structure
  ##with proper str format and len value. 
  def test_push_back_on_empty_deque_string(self):
    self.__deque.push_back('Liam')
    self.assertEqual('[ Liam ]', str(self.__deque))
  
  def test_push_back_on_empty_deque_length(self):
    self.__deque.push_back('Liam')
    self.assertEqual(1, len(self.__deque))  
  
  def test_push_back_twice_on_deque_string(self):
    self.__deque.push_back('Coolguy')
    self.__deque.push_back('Liam')
    self.assertEqual('[ Coolguy, Liam ]', str(self.__deque))
  
  def test_push_back_twice_on_deque_length(self):
    self.__deque.push_back('Coolguy')
    self.__deque.push_back('Liam')
    self.assertEqual(2, len(self.__deque))  
    
  def test_push_back_thrice_on_deque_string(self):
    self.__deque.push_back('Coolguy')
    self.__deque.push_back('Liam')
    self.__deque.push_back('duh')
    self.assertEqual('[ Coolguy, Liam, duh ]', str(self.__deque))
  
  def test_push_back_thrice_on_deque_length(self):
    self.__deque.push_back('Coolguy')
    self.__deque.push_back('Liam')
    self.__deque.push_back('duh')
    self.assertEqual(3, len(self.__deque))  
  
  ##pop back tests starting with empty deque working up to deque with 3
  ##entries. Test ensures pop back function creates correct deque structure
  ##with proper str format and len value
  def test_pop_back_empty_deque(self):
    with self.assertRaises(IndexError):
      pop = self.__deque.pop_back()
      self.assertEqual('[ ]', str(self.__deque))  
  
  def test_pop_back_single_deque_string(self):
    self.__deque.push_back('Liam')
    pop = self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))
  
  def test_pop_back_single_deque_popvalue(self):
    self.__deque.push_back('Liam')
    pop = self.__deque.pop_back()
    self.assertEqual('Liam', pop)
  
  def test_pop_back_single_deque_length(self):
    self.__deque.push_back('Liam')
    pop = self.__deque.pop_back()
    self.assertEqual(0, len(self.__deque))  
  
  def test_pop_back_double_deque_string(self):
    self.__deque.push_back('Coolguy')
    self.__deque.push_back('Liam')
    pop = self.__deque.pop_back()
    self.assertEqual('[ Coolguy ]', str(self.__deque))
  
  def test_pop_back_double_deque_popvalue(self):
    self.__deque.push_back('Coolguy')
    self.__deque.push_back('Liam')
    pop = self.__deque.pop_back()
    self.assertEqual('Liam', pop)

  def test_pop_back_double_deque_length(self):
    self.__deque.push_back('Coolguy')
    self.__deque.push_back('Liam')
    pop = self.__deque.pop_back()
    self.assertEqual(1, len(self.__deque))  
  
  
  ##peek back tests starting with empty deque up to deque with 2 entries. 
  ##Tests to ensure peek back function is pulling correct data without 
  ##affecting entries in deque. 
 
  def test_peek_back_empty_deque_string(self):
    with self.assertRaises(IndexError):
      peek = self.__deque.peek_back()
      self.assertEqual(0, len(self.__deque))
  
  def test_peek_back_empty_deque_length(self):
    with self.assertRaises(IndexError):
      peek = self.__deque.peek_back()
      self.assertEqual(0, len(self.__deque))   
  
  def test_peek_back_single_deque_string(self):
    self.__deque.push_back('Coolguy')
    peek = self.__deque.peek_back()
    self.assertEqual('[ Coolguy ]', str(self.__deque))  
  
  def test_peek_back_single_deque_peekvalue(self):
    self.__deque.push_back('Coolguy')
    peek = self.__deque.peek_back()
    self.assertEqual('Coolguy', peek)

  def test_peek_back_single_deque_length(self):
    self.__deque.push_back('Coolguy')
    peek = self.__deque.peek_back()
    self.assertEqual(1, len(self.__deque))   
  
  def test_peek_back_double_deque_string(self):
    self.__deque.push_back('Coolguy')
    self.__deque.push_back('Liam')
    peek = self.__deque.peek_back()
    self.assertEqual('[ Coolguy, Liam ]', str(self.__deque))
  
  def test_peek_back_double_deque_peekvalue(self):
    self.__deque.push_back('Coolguy')
    self.__deque.push_back('Liam')
    peek = self.__deque.peek_back()
    self.assertEqual('Liam', peek)
  
  def test_peek_back_double_deque_length(self):
    self.__deque.push_back('Coolguy')
    self.__deque.push_back('Liam')
    peek = self.__deque.peek_back()
    self.assertEqual(2, len(self.__deque))   
  
#Stack Tests
  ##push tests starting with empty stack up to stack with 2 entries 
  def test_push_empty_stack_string(self):
    self.__stack.push('Liam')
    self.assertEqual('[ Liam ]', str(self.__stack))
  
  def test_push_empty_stack_length(self):
    self.__stack.push('Liam')
    self.assertEqual(1, len(self.__stack))  
  
  def test_push_single_stack_string(self):
    self.__stack.push('Liam')
    self.__stack.push('Coolguy')
    self.assertEqual('[ Coolguy, Liam ]', str(self.__stack))
  
  def test_push_single_stack_length(self):
    self.__stack.push('Liam')
    self.__stack.push('Coolguy')
    self.assertEqual(2, len(self.__stack))   
  
  def test_push_multiple_stack_string(self):
    self.__stack.push('Liam')
    self.__stack.push('Coolguy')
    self.__stack.push('here')
    self.assertEqual('[ here, Coolguy, Liam ]', str(self.__stack))
  
  def test_push_multiple_stack_length(self):
    self.__stack.push('Liam')
    self.__stack.push('Coolguy')
    self.__stack.push('here')
    self.assertEqual(3, len(self.__stack)) 
  
  ##pop tests
  def test_pop_empty_stack(self):
    with self.assertRaises(IndexError):
      pop = self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))
  
  def test_pop_single_stack_string(self):
    self.__stack.push('Liam')
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))
  
  def test_pop_single_stack_length(self):
    self.__stack.push('Liam')
    self.__stack.pop()
    self.assertEqual(0, len(self.__stack))    
  
  def test_pop_double_stack_string(self):
    self.__stack.push('Liam')
    self.__stack.push('Coolguy')
    pop = self.__stack.pop()
    self.assertEqual('[ Liam ]', str(self.__stack))
  
  def test_pop_double_stack_popvalue(self):
    self.__stack.push('Liam')
    self.__stack.push('Coolguy')
    pop = self.__stack.pop()
    self.assertEqual('Coolguy', pop)    
  
  def test_pop_double_stack_length(self):
    self.__stack.push('Liam')
    self.__stack.push('Coolguy')
    pop = self.__stack.pop()
    self.assertEqual(1, len(self.__stack))    
  
  ##peek tests
  def test_peek_empty_stack(self):
    with self.assertRaises(IndexError):
      peek = self.__stack.peek()
    self.assertEqual('[ ]', str(self.__stack))
    
  def test_peek_single_stack_string(self):
    self.__stack.push('Liam')
    peek = self.__stack.peek()
    self.assertEqual('[ Liam ]', str(self.__stack))
  
  def test_peek_single_stack_peekvalue(self):
    self.__stack.push('Liam')
    peek = self.__stack.peek()
    self.assertEqual('Liam', peek)
  
  def test_peek_single_stack_length(self):
    self.__stack.push('Liam')
    peek = self.__stack.peek()
    self.assertEqual(1, len(self.__stack))  
  
  def test_peek_double_stack_string(self):
    self.__stack.push('Coolguy')
    self.__stack.push('Liam')
    peek = self.__stack.peek()
    self.assertEqual('[ Liam, Coolguy ]', str(self.__stack))
  
  def test_peek_double_stack_peekvalue(self):
    self.__stack.push('Coolguy')
    self.__stack.push('Liam')
    peek = self.__stack.peek()
    self.assertEqual('Coolguy', peek) 
  
  def test_peek_double_stack_length(self):
    self.__stack.push('Coolguy')
    self.__stack.push('Liam')
    peek = self.__stack.peek()
    self.assertEqual(2, len(self.__stack))  
  
  #Queue Tests
  ##Enqueue tests
  def test_enq_empty_string(self):
    self.__queue.enqueue('Liam')
    self.assertEqual('[ Liam ]', str(self.__queue))
  
  def test_enq_empty_length(self):
    self.__queue.enqueue('Liam')
    self.assertEqual(1, len(self.__queue))  
  
  def test_enq_multiple_string(self):
    self.__queue.enqueue('Liam')
    self.__queue.enqueue('Coolguy')
    self.assertEqual('[ Liam, Coolguy ]', str(self.__queue)) 
  
  def test_enq_multiple_length(self):
    self.__queue.enqueue('Liam')
    self.__queue.enqueue('Coolguy')
    self.assertEqual(2, len(self.__queue))   




if __name__ == '__main__':
  unittest.main()
  

