T = int(raw_input(""))
for x in range(0,T):
    a = raw_input()
    a = a.split()
    P = int(a[1])
    N = int(a[0])
    b = 1
    for x in xrange (1, ((3*N)+1)):
        b = b*x
    s = 1
    for x in xrange (1, N+1):
        s = s * 6
    p = (b/s)%P   
    print p
