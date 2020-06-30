for i in range(1, 1 + input()):
    cset1 = set()
    cset2 = set()
    ca = []
    for j in range(1, 1 + input()):
        ca += [raw_input().strip().split()]
        #print ca
        if not (ca[-1][0] in cset1 or ca[-1][1] in cset2):
            cset1 |= {ca[-1][0]}
            cset2 |= {ca[-1][1]}
            ca.pop()
    for ci in range(len(ca) - 1, -1, -1):
        if not (ca[ci][0] in cset1 and ca[ci][1] in cset2):
            cset1 |= {ca[ci][0]}
            cset2 |= {ca[ci][1]}
            ca.pop(ci)
    #print ca
    print "Case #{}: {}".format(i,len(ca))
