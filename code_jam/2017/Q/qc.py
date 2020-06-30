def f(fa, fb, fc, fd, fe):
    if fb != fc:
        for fi in fd:
            fe += g(fi)
        return f(fa, fb + 1, fc, fe, [])
    else:
        fd.sort()
        fd.reverse()
        return fd[fa - 1]

def g(ga):
    gb = ga - 1
    gc = int(gb/2)
    return [gb - gc, gc]

for i in range(1, 1 + input()):
    ca = map(int, raw_input().split())
    cb = len(bin(ca[0])) - 2
    cc = 2 ** (cb - 2)
    ce = len(bin(ca[1])) - 2
    cd = ca[1] - 2 ** (ce - 1) + 1
    if ca[0] - ca[1] < max(cc, ca[0] - cc * 2 + 1):
        cz = 1
    else:
        cz = f(cd, 1, ce, [ca[0]], [])

    print("Case #{}: {} {}".format(i, g(cz)[0], g(cz)[1]))
