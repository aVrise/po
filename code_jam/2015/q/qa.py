for i in range(1, 1 + input()):
    ca = raw_input().split()
    cb = ca[1]
    cc = int(cb[0])
    cz = 0
    #print cb

    for ci in range(1, len(cb)):
        #print ci
        if cc < ci:
            cz += ci - cc
            cc = ci
        cc += int(cb[ci])

    print('Case #{}: {}'.format(i, cz))
