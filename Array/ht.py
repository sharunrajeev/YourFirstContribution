# Python3 program to maximize
# array sum after k operations.

# This function does k operations on array
# in a way that maximize the array sum.
# index --> stores the index of current
# minimum element for j'th operation


def maximumSum(arr, n, k):

	# Modify array K number of times
	for i in range(1, k + 1):

		min = +2147483647
		index = -1

		# Find minimum element in array for
		# current operation and modify it
		# i.e; arr[j] --> -arr[j]
		for j in range(n):

			if (arr[j] < min):

				min = arr[j]
				index = j

		# this the condition if we find 0 as
		# minimum element, so it will useless to
		# replace 0 by -(0) for remaining operations
		if (min == 0):
			break

		# Modify element of array
		arr[index] = -arr[index]

	# Calculate sum of array
	sum = 0
	for i in range(n):
		sum += arr[i]
	return sum


# Driver code
arr = [-2, 0, 5, -1, 2]
k = 4
n = len(arr)
print(maximumSum(arr, n, k))

# This code is contributed by george
