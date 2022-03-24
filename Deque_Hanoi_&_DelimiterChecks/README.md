# Use Deque to solve Tower of Hanoi and create a program to perform Delimeter checks
## What is the Tower of Hanoi
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
3. No disk may be placed on top of a smaller disk.

## What is a Delimeter Check program?
The program allows users to check if their files have balanced delimeters, a useful tool to avoid frustrating errors!

## How to Run:
Download the file on your machine. Then navigate to the file using your terminal and run the command "python3 Hanoi.py" to see the algorithm solve the Tower of Hanoi using our new created classes action! 
To use the Delimiter check run the command "python3 Delimiter_Check.py _______.py" where the blank space is for you to insert any file name you'd like to check. 

If you would just like to leverage any of the classes feel free to download only that file and reference it like you would any other built in class. Just make sure you import the file into the code you're using it in.

## Summary of work
The Hanoi and Delimiter Check solutions utilize the Stack class I created, which in turn utilizes the Deque class I created. Overall the two solutions were the easiest part of the work and the real value comes in terms of the classes I created. 

## Performance Characteristics
Worst Case Performance:
Str: both the ARR and LL Deque types have similar string functions and the processing is linear. 
Len: similar to above
Push_front: 
Linked List class will work better for operations that involve entering the back of the dequeue 

Tower of Hanoi: Operates in Linear Time 


## Test Cases
I organized my test cases into empty tests, Deque Type tests, Stack Type and Queue Type tests. It is worth noting I did not write individual test cases for the LL Deque Type and ARR Deque type as they both can be tested with the existing cases if the initial parameters are changed in DSQ_Test.py and Deque_Generator.py. The empty tests consisted of simply testing to ensure the string method in each type was working properly and outputting correctly.  Next I tested the Deque class. My Deque class testing can be broken up into categories by function: push_front, pop_front, peek_front, push_back, pop_back, and peek_back. Each one of these testing categories followed the same procedure in order to ensure consistency of testing rigor.  The procedure was to test the function first on empty deque then test the function on a deque with a single entry then test the function on a deque with multiple entries.  These 3 classes of deques were used in test cases that checked to ensure that for each deque the function was outputting the correct string output, length and if applicable return value.  These test cases are very effective at ensuring all functions are working correctly because each deque type (empty, single or multiple) is tested for string output, length and if applicable return output.  In other words each function has a 2 or three tiered test for 3 types of deques. An extremely rigorous approach. There is one aspect worth noting.  When testing the ARR Deque type 5 failures arise in the test cases.  These failures are a result of the way the test cases are written and not a failure of the ARR Deque class itself.  These failures are the result f the LL Deque class pulls index errors while the ARR Deque does not.  