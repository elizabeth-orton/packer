#you can recurse in python?? who knew
# Binary Search
# Pre-Condition: parameters are list, target item, left bound, right bound
# Post-Condition: function returns the index of target or -1 if not found
def search(list, target, a, b):
	middle = a + (b - a) // 2
	print("Search called")
	if b <= a:
		return -1
	elif list[middle] < target:
		a = middle + 1
	elif list[middle] > target:
		b = middle
	elif list[middle] == target:
		return middle	
	
  # this is a recursive search because the method search() 
  # calls itself
	return search(list, target, a, b)

# List of length 4
myList = [0, 3, 4, 9]
print("Searching length of 4")
print(search(myList, 3, 0, len(myList)))
print()
print(search(myList, 2, 0, len(myList)))