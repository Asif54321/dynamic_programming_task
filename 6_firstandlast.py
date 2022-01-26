'''
6. Given a sorted array arr containing n elements with possibly duplicate
elements, the task is to find indexes of first and last occurrences of an
element x in the given array.
Example:
Input:n=9, x=5arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
Output: 2 5Explanation: First occurrence
of 5 is at index 2 and last occurrence of 5 is at index 5.

'''

# last occurrences of a number in
# a given sorted array

# if x is present in arr[] then
# returns the index of FIRST
# occurrence of x in arr[0..n-1],
# otherwise returns -1
def first(arr, low, high, x, n) :
	if(high >= low) :
		mid = low + (high - low) // 2
		if( ( mid == 0 or x > arr[mid - 1]) and arr[mid] == x) :
			return mid
		elif(x > arr[mid]) :
			return first(arr, (mid + 1), high, x, n)
		else :
			return first(arr, low, (mid - 1), x, n)
	
	return -1


# if x is present in arr[] then
# returns the index of LAST occurrence
# of x in arr[0..n-1], otherwise
# returns -1
def last(arr, low, high, x, n) :
	if (high >= low) :
		mid = low + (high - low) // 2
		if (( mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x) :
			return mid
		elif (x < arr[mid]) :
			return last(arr, low, (mid - 1), x, n)
		else :
			return last(arr, (mid + 1), high, x, n)
			
	return -1
	

# Driver program
arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
n = len(arr)

x = 5
print("First Occurrence = ",
	first(arr, 0, n - 1, x, n))
print("Last Occurrence = ",
	last(arr, 0, n - 1, x, n))


'''
Time Complexity : O(log n) 
Auxiliary Space : O(Log n) 
'''