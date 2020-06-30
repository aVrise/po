def f(fa, fb):
    fz = 1
    for fi in fa:
        fz *= fb[fi] 
        if fz < 10**(-7):
            return 0
    return fz

#def g(ga):


for i in range(1, 1 + input()):
    ca = map(int, raw_input().split())
    cb = raw_input()
    cc = raw_input()
    cd = set(cb)
    ce = set(cc)
    cf = list(cb)
    cg = list(cc)
    cz = 0.0
    cx = 0.0
    cy = 0.0

    if len(cd|ce) > len(cd):
        cz = 0.0
    else:
        for ci in range(1, len(cg)):
            if cg[ci:] == cg[0:len(cg[ci:])]:
                break
        else:
            ci = 0
        cmax = (ca[2] - ca[1])/(len(cg) - ci) + 1

        if len(cd) == 10000:
            cz = 0.0
        else:
            cdic = {}
            for cj in cd:
                cdic[cj] = 1.0 * cb.count(cj) / len(cb)

            ch = f(cg, cdic) 
            chh = f(cg[ci:], cdic) 
            print cdic, ch, chh
            for cj in range(cmax, 0, -1):
                cy += cx
                cx = (ch * chh ** (cj - 1)) - cy
                cz += cj * cx
            cz = cmax - cz
    print "Case #{}: {}".format(i, cz)
        