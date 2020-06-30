for i in range(1, 1 + input()):
    ca = map(int, raw_input().split())
    cz = ((ca[1] - 1)/ca[2]) + (ca[2]) + (ca[0] - 1) * (ca[1]/ca[2])

    print "Case #{}: {}".format(i, cz)