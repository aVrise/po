import sys


def f(fa, fb):
    if fb == 0.0:
        return fa
    else:
        fa.sort()
        fc = fa.count(fa[-1])
        if fc == len(fa):
            return [fa[0] + fb / len(fa)] * len(fa)
        fd = fa[-(fc + 1)] - fa[-1]
        if fb <= fc * fd:
            for fi in range(1, fc + 1):
                fa[-fi] += fb / fc
            fb = 0.0
        else:
            for fi in range(1, fc + 1):
                fa[-fi] += fd
            fb -= fc * fd
        return f(fa, fb)


# sys.setrecursionlimit(10000)
for i in range(1, 1 + input()):

    ca = map(int, raw_input().split())
    cb = float(input())
    cc = map(float, raw_input().split())

    if (max(cc) * ca[0] - sum(cc)) <= cb:
        cb -= (max(cc) * ca[0] - sum(cc))
        cc = [max(cc) + cb / ca[0]] * ca[0]
    else:
        cc = f(cc, cb)
    cz = 1
    for ci in cc:
        cz *= ci
    print "Case #{}: {}".format(i, cz)
