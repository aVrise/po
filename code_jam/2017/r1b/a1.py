for i in range(1, 1+input()):
    ca = map(int, raw_input().split())
    cb = []
    for ci in range(ca[1]):
        cj = map(float, raw_input().split())
        cb += [(ca[0]-cj[0])/cj[1]]
    cz = ca[0]/max(cb)
    print "Case #{}: {}".format(i, cz)

