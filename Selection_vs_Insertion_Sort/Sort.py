#Liam Cashel
#Project 1

import random
import time

#evaluates values to the left of current cell and moves any larger values
#encountered to the right
def insertion_sort(arr):
    for x in range(1, len(arr)):
        place = arr[x]
        index = x
        while arr[index-1] > place and index > 0:
            arr[index]=arr[index-1]
            index = index - 1
        arr[index] = place

#finds the minimum value from (k, n-1) in the array and if it is less than 
#the current value the values are swapped
def selection_sort(arr):
    for x in range(len(arr)-1):
        indx = x
        countMin = indx
        while indx < len(arr)-1:
            indx = indx + 1            
            if arr[countMin] > arr[indx]:
                countMin = indx
        temp = arr[x]
        arr[x] = arr[countMin]
        arr[countMin] = temp  

#adapted from the Ceaser Cipher example
if __name__ == '__main__':
            
    arr_len = [1000, 2500, 5000, 7500, 10000]

    #Increasing order test
    for value in arr_len:
        #creates increasing order array
        arr = [None] * value
        entry = 0
        for number in range(value):
            arr[number] = number
            number = number + 1
        
        arr_Sel = arr
        arr_Ins = arr
        
        #insertion sort for increasing order timing
        start = time.clock()
        insertion_sort(arr_Ins)
        end = time.clock()
        print("Array Size: " + str(value))
        print('Increasing Insertion: ' + '{:.20f}'.format(end - start))
    
        #selection sort for increasing order timing
        start = time.clock()
        selection_sort(arr_Sel)
        end = time.clock() 
        print('Increasing Selection: ' + '{:.20f}'.format(end - start))
        print()   
        
    #decreasing order test
    for value in arr_len:
        #creates array decreasing at with a negative-one step
        arr = [None] * value
        number = value
        index = 0
        while number > 0:
            arr[index] = number
            number = number - 1
            index = index + 1
            
        arr_Sel = arr
        arr_Ins = arr
        
        #insertion sort for decreasing order timing
        start = time.clock()
        insertion_sort(arr_Ins)
        end = time.clock()
        print("Array Size: " + str(value))
        print('Decreasing Insertion: ' + '{:.20f}'.format(end - start))

        #selection sort for increasing order timing
        start = time.clock()
        selection_sort(arr_Sel)
        end = time.clock() 
        print('Decreasing Selection: ' + '{:.20f}'.format(end - start))
        print()        
        
    #random order test
    for value in arr_len:
        #creates array filled with random values
        arr = [None] * value
        for number in range(value):
            rand = random.randint(0, 100000)
            arr[number] = rand
        
        arr_Sel = arr
        arr_Ins = arr
        
        #insertion sort for random order timing
        start = time.clock()
        insertion_sort(arr_Ins)
        end = time.clock()
        print("Array Size: " + str(value))
        print('Random Insertion: ' + '{:.20f}'.format(end - start))

        #selection sort for random order timing
        start = time.clock()
        selection_sort(arr_Sel)
        end = time.clock() 
        print('Random Selection: ' + '{:.20f}'.format(end - start))
        print()              
            
