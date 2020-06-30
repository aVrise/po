for i in range(1, 1 + input()):
    ca = raw_input().strip().split()
    ca = map(int, ca)
    #print ca

    if ca[0] == 1:
        cz = [1]
    elif ca[1] == 1:
        cz = range(1, 1 + ca[0])
    elif ca[0] == 2:
        cz = [2]
    else:
        cb, cc = divmod(ca[0], ca[1])
        #print cb, cc
        cz = []
        if cb != 0:
            for ci in range(cb):
                ck = ci * ca[0] ** (ca[1] - 1)
                for cii in range(1, ca[1] + 1):
                    ck += (ci * ca[1] + cii - 1) * ca[0] ** (ca[1] - cii)
                cz.append(ck + 1)
                #cz.append(ci * ca[1] * (ca[0] ** (ca[1] - 1)) * 0 + (ca[1] - 2 + ci * ca[1]) * (ca[0] + 1) + 2)
            if cc != 0:
                ck = cb * ca[0] ** (ca[1] - 1)
                for cii in range(1, cc + 1):
                    ck += (cb * ca[1] + cii - 1) * ca[0] ** (ca[1] - cii)
                cz.append(ck + 1)
        else:
            for cii in range(1, cc + 1):
                ck += (cii - 1) * ca[0] ** (ca[1] - cii)
            cz.append(ck + 1)
    print cz
    ct = ca[0] ** ca[1]
    assert max(cz) <= ct
    #print cz
    cz = map(str, cz)
    if len(cz) <= ca[2]:
        print "Case #{}: {}".format(i, ' '.join(cz))
    else:
        print "Case #{}: IMPOSSIBLE".format(i)
