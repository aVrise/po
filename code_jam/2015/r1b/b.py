for i in range(1, 1 + input()):
    ca = map(int, raw_input().split())
    cd = (ca[0] * ca[1] + 1)/2
    if ca[2] <= cd:
        cz = 0
    else:
        if ca[0]==ca[1]==3 and ca[2]==8:
            cz = 8
        else:
            cb = (ca[1] % 2) + (ca[0] % 2)
            cc = ca[0] + ca[1] - 2
            if 1 in ca[0:2]:
                cz = 2*(ca[2]-cd)
            else:
                if ca[2] > cc + cd:
                    cz = 3*cc + 4*(ca[2]-cd-cc)
                else:
                    cz = 3*(ca[2]-cd)
                if cb != 2:
                    cz -= min(2, ca[2]-cd)
    print "Case #{}: {}".format(i, cz)
