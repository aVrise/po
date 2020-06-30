from math import pi

for i in range(1, 1 + input()):
    ca = map(int, raw_input().split())
    cb = []
    cz = 0
    for ci in range(ca[0]):
        cj = map(int, raw_input().split())
        cb.append([cj[0], 2 * cj[0] * cj[1]])
    for ci in range(ca[0]):
        cd = [cb[ci][0]**2, cb[ci][1]]
        cc = cb[:ci]+cb[ci+1:]
        cc.sort(key=lambda x: x[1], reverse=True)
        for ck in cc:
            if len(cd) > ca[1]:
                break
            if ck[0] > cb[ci][0]:
                continue
            else:
                cd.append(ck[1])
        cz = max(cz, sum(cd))
    print "Case #{}: {:.10f}".format(i, 1.0 * cz * pi)
