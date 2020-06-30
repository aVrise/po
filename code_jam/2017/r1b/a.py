for i in range(1, 1 + input()):
    ca = map(int, raw_input().split())
    cb = []
    for ci in range(ca[1]):
        cb += [map(int, raw_input().split())]
    cb.sort(reverse=True)

    cc = 1.0*(ca[0]-cb[0][0])/cb[0][1]
    for ci in range(1, ca[1]):
        if cb[ci][1] <= cb[ci-1][1] or 1.0*(cb[ci - 1][0] - cb[ci][0])/(cb[ci][1]-cb[ci - 1][1]) >= cc:
            cc = 1.0*(ca[0]-cb[ci][0])/cb[ci][1]
    cz = ca[0]/cc
    #print 1.0 * cb[ci][0]/(cz-cb[ci][1]), cc

    # for ci in range(ca[1]):
    #     if cz-cb[ci][1] > 0:
    #         print 1.0 * cb[ci][0]/(cz-cb[ci][1]), cc
    #         assert 1.0 * cb[ci][0]/(cz-cb[ci][1]) - cc >= - 10 ** (-10)

    print "Case #{}: {}".format(i, cz)
