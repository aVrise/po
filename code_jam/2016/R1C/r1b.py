for i in range(input()):
    ca = map(int, raw_input().strip().split())
    cb = ca[0] - 2
    print "Case #{}: ".format(i + 1),
    if ca[0] == 2:
        if ca[1] > 1:
            print "IMPOSSIBLE"
        else:
            print "POSSIBLE"
            print "01"
            print "00"
    elif cb ** 2 < ca[1]:
        print "IMPOSSIBLE"
    else:
        print "POSSIBLE"
        cc = []
        cia = ca[1]
        cib =0
        while  cia != 0:
            if cia & 1 == 1:
                cc.append(cib)
            cia >>= 1
            cib += 1
        cd = 1
        cc.reverse()
        for ci in cc:
            for cj in range(ci, -1, -1):
                print "0" * cd + "1" * cj + "0" * (ca[0] - cd - cj - 1) + "1"
                cd += 1
        while not cd > ca[0]:
            print "0" * ca[0]
            cd += 1
