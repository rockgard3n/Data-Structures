# Solving the Josephus Problem with Linked Lists
## What is the Josephus Problem?
We need to find the correct position to avoid execution! Given a group of N people arranged in a circle where every M'th man will be executed. These executions will continue until only one person remains. So how do we find the position L(n,m) in which you should stand in order to be the last survivor? 

To solve the problem I utilized Linked Lists and created a class "Linked_List" within the file "Linked_List.py" and utilized it in "Josephus.py" 

## How to Run:
Download the file on your machine. Then navigate to the file using your terminal and run the command "python Josephus.py" to see the algorithm in action! 
If you would just like to leverage the linked_list class feel free to download only that file and reference it like you would any other built in class. Just make sure you import the file into the code you're using it in by including the line "from Linked_List import Linked_List" 

## Summary of work and analysis of solution 
The Josephus solution combines multiple functions in the Linked_Class.  It iterates through a for loop to remove a certain value each iteration and thus is at least constant time.  However, both functions within the loop operate under constant time.  The rotate method was already defined as constant time but the removal function is a special case because the element it is removing is always position zero, thus it is constant time. The get element function does not affect the performance because it is only called once.  Since the removal function is within the for loop each iteration is a smaller list.  Thus the Josephus solution operates under linear performance so O(n)

## Performance Characteristics of the Linked List Class
Both __init__ methods are initialized by the Linked_List class in order to set up the class object and are intuitively O(1) [constant time].

The __len__ method simply calls the ._size method.  Since the _size method is linear so is the _len_ method: O(n) [linear performance]. 

The append_element_at(…) method performs the same task regardless of the size of the list (ignoring a one line increase in performance if the list is empty).  It adds a value to the end of a list through the sentinel nodes to avoid iterating.  Therefore it is O(1) [linear performance].

Since the insert_element_at(…) method uses an iterating for loop to find the indexed position to insert a value it is inherently O(n) [linear performance]. 

Similarly the remove_element_at(…) method uses an iterating for loop to find an indexed position, except in this case to remove it.  Thus it is O(n) [linear performance].

Similarly the get_element_at(…) method uses an iterating for loop to find an indexed position, except in this case to only retrieve it.  Thus it is O(n) [linear performance].

The rotate_left(…) method performs the same task regardless of the size of the list and rotates the nodes in the list using the sentinel nodes rather than iteration, thus it’s performance is constant time (O(1)). 

The __str__ method uses a for loop to iterate through the linked list to perform is function and thus operates with O(n) performance. 

The __iter__ method simply declares a variable name for a position and inherently operates under constant time. 

The __next__ method iterates through the entire list one step at a time and thus in n steps therefore its performace is O(n).

## Test Cases
My test cases can be broken down into seven sections: empty list test, append tests, insertion tests, removal tests, get element tests, loop tests, and rotate tests. These seven sections cover the areas of the class that are not inherently checked by another function in the class (such as the __iter__ function).  The __len__ and __str__ functions were tested over all seven sections.  This was because the __str__ function allowed for the easiest way to check each test result, which was printing, and the __len__ function offered a useful indicator of whether the append, remove and insert functions were working correctly.  
	I performed an empty list test because an empty list creates an exception for many of the functions in the Linked_List class, thus it was vital to test to see if these exceptions were correct.  The tests I conducted are sufficient because they were conducted on the three functions (get_element_at, insert_element_at, remove_element_at) that are supposed to pull IndexErrors if used on empty list.  The tests on these three functions are complete because all three successfully raised the correct errors. Additionally, as a precaution, the rotate_left function was tested to ensure when handed an empty list it did nothing and simply returned the list.  
	I performed a series of tests on the append_element function.  These tests are complete because I tested the function on empty lists and on numerous n-valued lists while also checking to ensure that the size of these lists were correct using the __len__ function.  
	I performed a number of tests on the insert_at_element function.  These tests are complete because I tested valid indexes as well as invalid indexes to ensure the function was returning the correct outputs.  The valid indexes are 0 – (n-1) so I tested the insertion function at some position less than n as well as at position 0 (to ensure it could append to head of a non-empty list).  The output of these two tests were compared with the list and list length prior to insertion to ensure they function performed properly.  Invalid indexes are any negative value and any value greater than or equal to n. Therefore, the two values tested were n and some negative number.  The outputs of these functions were, as expected, IndexErrors. 
	The tests performed on the remove_at_index function follow the same structure as the insertion tests with the addition of checking to ensure the removal function also returned the value removed.  Thus the testes on the remove function are complete as they test all requirements of the function. 
	The tests performed on the get_element_at function follow the same structure as the insertion and removal tests: testing valid and invalid indices while ensuring the outputs match the specifications of the class. Thus the tests are complete. 
	Several loop tests were also performed on empty lists, lists of size 1, lists of size 2 and lists of size 3 and upwards.  These sized lists were tests because empty lists and size 1 lists should be unaffected by the function.  Size 2 lists were tested as an extra precaution to ensure the function operated correctly and size 3+ lists were tested as they are the primary input of the function.  Since the method of rotating a function of a list of size 3 or greater is identical the loop tests are complete. 
	The __len__ and __str__ functions while lacking their own specific test section were pervasive through all of the tests and therefore were tested rigorously under all relevant situations.  Thus the tests are complete. 
