for i in range(1, 1 + input()):
    ca = raw_input().split()
    cb = int(ca[1])
    ca = list(ca[0])
    cc = []
    for ci in ca:
        if ci == '+':
            cc.append(1)
        else:
            cc.append(-1)

    cx = 1
    cz = 0
    while -1 in cc:
        cl = cc.index(-1)
        if cl + cb > len(cc):
            cx = 0
            break
        else:
            cm = [-1 * x for x in cc[cl:cl + cb]]
            cm = cm[cm.index(-1):] if -1 in cm else []
            cc = cm + cc[cl + cb:]
            cz += 1

    if cx == 0:
        cz = "IMPOSSIBLE"

    print("Case #{}: {}".format(i, cz))
