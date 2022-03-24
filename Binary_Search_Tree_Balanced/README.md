# Unbalanced Binary Search Tree
## What is a Binary Search Tree?
A binary search tree (BST) is a tree comprised of nodes. Each node has exactly two children, where the left child is always less than the parent and the parent is alway less than the right child. The term "balance" comes from scenarios where you could have a long tail of children on one parent node but not the other. To combat this I added a balance function to my BST class that rotates nodes recursively to balance the tree. 

![](balanced-tree.png)

## How to Run:
Download the file on your machine. Then navigate to the file using your terminal and run the command "python3 Fraction.py" to see an example of the class in action. 

If you would just like to leverage the Balanced BST class feel free to download only that file and reference it like you would any other built in class. Just make sure you import the file into the code you're using it in.

## Performance Characteristics of the Linked List Class
I added two new lines of code to my update_height function from my unbalanced BST class so that it would also update the balance of the node, this had no effect on performance and it remained operating at O(1). I also added left and right rotation functions which also operate at O(1) because they are just a series of for loops with no recursion, however there is a slight time improvement if the tree is already balanced because it can skip the update_height call at the end of the function.  The worst case for the insert method would be O(logn) because the height of the tree would be no more than 2log(n)+2, which becomes log(n) after constants are removed. Similarly the worst case for removal would be O(logn). This is because the rotations and the updating-height functions are all constant time. The runtime of the to_list function is similar to the other 3 traversals and for the same reason as I discussed in my last right up is O(n).  Finally the fraction class functions I wrote all operate in O(1) time. 


## Test Cases
The test cases for balanced BST were simpler than for when I made my initial unbalanced BST class because we already knew we had a fully function binary search tree class thanks to the previous test cases.  So this time I focused on exclusively aspects of the class that were affected by the balance function.  Each section of my test code contains 5 individual tests.  3 of these tests check to make sure in-order, pre-order and post-order all check out to make sure our tree is correctly formed.  I also include a height check as an extra measure to ensure the tree is correctly formed.  Finally each section has a to_list test because this was a new function for our class and it seemed prudent to test it in as many cases as possible.   I began tests with insertions, initially creating a tree that required a single right rotation, then I tested trees that required single left rotation and then the final tests for single rotations was to test a rotation that required a “floating” node.  These tests insured that the basics of my _left_rotation and _right_rotation functions were working correctly so I could move on to double rotations to ensure the rest of my _balance function was also working correctly.  Next I did removal tests to ensure that my class could still correctly create an empty tree. Then I tested removing a childless tree as this is the least complicated removal and should be attempted first. Finally for the removal functions I removed the node as this is a complicated position for the balance function to work with as well as easy for me to understand where an error originated.  Then to conclude my test cases I created a series of insertions and removals that necessitated a large number of various different rotations as a final check of the new functions. 