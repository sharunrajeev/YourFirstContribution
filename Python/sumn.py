def minSpacePreferLarge(w, m, n):

	# initialize result variables
	num_m = 0
	num_n = 0
	rem = w

	# p and q are no of shelves of length m &
	# n respectively. r is the remainder uncovered
	# wall length
	p = w//m
	q = 0
	rem=w%m;
	num_m=p;
	num_n=q;
	min_empty=rem;
	while (w >= n):
		q += 1;
		w-= n;
		p = w // m
		r = w % m
		if (r <= rem):
			num_m = p
			num_n = q
			rem = r
		q += 1
		w -= n
	print( str(int(num_m)) + " " + str(num_n) + " " + str(rem))

# Driver code
w = 24
m = 3
n = 5
minSpacePreferLarge(w, m, n)

w = 24
m = 4
n = 7
minSpacePreferLarge(w, m, n)
