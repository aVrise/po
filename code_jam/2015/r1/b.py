def gcd(a, b):
    r = a % b
    if r:
        return gcd(b, r)
    else:
        return b
#print gcd(13, 6)

def lcm(a, b):
    return a * b / gcd(a, b)
#print lcm(12, 6)

def lcmAll(seq):
    return reduce(lcm, seq)

for i in range(1, 1 + input()):
    ca = map(int, raw_input().split())
    cb = map(int, raw_input().split())
    cc = len(cb)
    cd = cb[:]
    ce = lcmAll(cd)
    cf = 0
    for cj in cd:
        cf += ce / cj
    ca[1] = ca[1] % cf

    if ca[1] == 0:
        cm = cd[0]
        for ci, cj in enumerate(cd):
            if cj <= cm:
                cn = ci
        cz = cn + 1
    elif ca[1] <= ca[0]:
        cz = ca[1]
    else:
        #print ca[1]
        while cc < ca[1]:
            ci = min(cd)
            ci = cd.index(ci)
            cd[ci] += cb[ci]
            cc += 1
        cz = ci + 1

    print("Case #{}: {}".format(i, cz))
