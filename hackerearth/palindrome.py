T = int(raw_input(""))
for x in range(0,T):
    a = raw_input()
    a = a.split()
    B = int(a[1])
    A = int(a[0])
    count = 0
    for x in xrange(A, B+1):
        c=str(x)
	z = c[::-1]
	if c == z:
            count += 1
    print count 
