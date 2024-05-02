from decorator import timed

# O(n2), or quadratic, in average/worst case. O(n) (linear) in best case.
# No extra space used
@timed
def bubbleSort(arr):
	n = len(arr)

	for i in range(n):
		for j in range(0, n - i - 1):
			
			# Range of the array is from 0 to n-i-1
			# Swap the elements if the element found 
			#is greater than the adjacent element
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

# O(n2) (quadratic)
# Some extra space is used
@timed	
def selectionSort(array, size):
	for s in range(size):
		min_idx = s
		
		for i in range(s + 1, size):

			# For sorting in descending order
			# for minimum element in each loop
			if array[i] < array[min_idx]:
				min_idx = i

		# Arranging min at the correct position
		(array[s], array[min_idx]) = (array[min_idx], array[s])

def quicksort_partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1

# Worst case O(n2) (quadratic), average case O(N log N) (log linear)
# No extra space used
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = quicksort_partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
		
@timed
def quickSort_wrapper(array, low, high):
	quickSort(array, low, high)
	
# O(magic)
@timed
def timSort(array):
	array.sort()