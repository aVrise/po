import itertools

def f(fa, fb, fc):
    #K, index, C
    if C == 1:
        return fa[fb]
    else:
        fi, fj = divmod(fb, len(fa) ** (C - 1))
        if fa[fi] == 0:
            return 0
        else:
            return f(fa, fj, fc - 1)

for i in range(1, 1 + input()):
    ca = raw_input().strip().split()
    ca = map(int, ca)
    if ca[0] == 1:
        cz = 1
    elif ca[0] == 2:
        cz = 2
    else:
        if ca[1] == 1:
            cz = ca[0]
        elif ca[1] == 2:
            cb = '1' * ca[0]
            cc = []
            cz = ca[0]
            cd = (len(ca[0]) ** ca[1]) / 2
            ce = ca[0] - 1
            for j in itertools.count(ce, 1):

    if cz <= ca[2]:
        print "Case #{}: {}".format(i, cz)
    else:
        print "Case #{}: IMPOSSIBLE".format(i)
