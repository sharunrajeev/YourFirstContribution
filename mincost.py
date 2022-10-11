# Python program to divide a board into m*n squares
def minimumCostOfBreaking(X, Y, m, n):

	res = 0

	# sort the horizontal cost in reverse order
	X.sort(reverse = True)
	# sort the vertical cost in reverse order
	Y.sort(reverse = True)
	# initialize current width as 1
	hzntl = 1; vert = 1

	# loop until one or both
	# cost array are processed
	i = 0; j = 0
	while (i < m and j < n):
	
		if (X[i] > Y[j]):
		
			res += X[i] * vert

			# increase current horizontal
			# part count by 1
			hzntl += 1
			i += 1
		
		else:
			res += Y[j] * hzntl

			# increase current vertical
			# part count by 1
			vert += 1
			j += 1

	# loop for horizontal array, if remains
	total = 0
	while (i < m):
		total += X[i]
		i += 1
	res += total * vert

	#loop for vertical array, if remains
	total = 0
	while (j < n):
		total += Y[j]
		j += 1
	res += total * hzntl

	return res
	
# Driver program
m = 5; n = 2
X = [2, 1, 3, 1, 4]
Y = [4, 1, 2]

print(minimumCostOfBreaking(X, Y, m-1, n-1))


# This code is contributed by Mathew Saju.
