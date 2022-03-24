from Linked_List.py import LinkedList
numbers = LinkedList(5,4,2,-5,3)

def insertion_sort2(numbers):
  for k in range(1, len(numbers)):
    cur = numbers.getelementat(k)
    j = k
    while j > 0 and numbers.getelementat(j) > cur:
      j = j - 1
    try:
      numbers.insertelementat( numbers.getelementat(j), k).removeelementat(numbers.getelementat(j), j-1) 
    except:
      numbers.appendelement(numbers.getelementat(j).removeelementat(numbers.getelementat(j), j-1))
  print(a)