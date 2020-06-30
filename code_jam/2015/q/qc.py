def f(fa, fc):
    global cb
    fy = 1
    fz = ['i', 'j', 'k']
    if fa == fz[fc]:
        return 1
    else:
        while fa != fz[fc]:
            if len(cb) == 0:
                return 0
            elif fa == cb[0] and len(cb) > 2:
                fa = cb[1]
                cb = cb[2:]
                fy *= -1
            elif fa != cb[0]:
                fa = fa + cb[0]
                if fa in cd.keys():
                    fa = cd[fa]
                else:
                    fa = cd[fa[::-1]]
                    fy *= -1
                if len(cb) > 0:
                    cb = cb[1:]
            else:
                return 0
        else:
            return fy


for i in range(1, 1 + input()):
    ca = map(int, raw_input().split())
    cb = raw_input() * ca[1]
    cd = {'ij' : 'k',
          'jk' : 'i',
          'ki' : 'j'
          }

    cj = 0
    cx = 1
    cy = 1
    cw = 0
    if ca[0] * ca[1] < 3:
        cx = 0
    while cj != 3 and cx != 0:
        cc = cb[0]
        cb = cb[1:]
        cx *= f(cc, cj)
        cj += 1
        if cx == 0:
            break

    if cx == 0:
        cz = 'NO'
    else:
        while True:
            while True:
                cm = cb.count("ji")
                cw += cm
                cb.replace("ji", "ij")
                cn = cb.count("ki")
                cw += cn
                cb.replace("ki", "ik")
                if cn == 0 and cm == 0:
                    break
            cm = cb.count("kj")
            cb.replace("kj", "jk")
            cw += cm
            if cm == 0:
                break

    cx *= -1 ** (cw % 2)
    cm1, cm2 = divmod(cb.count('i'), 2)
    cn1, cn2 = divmod(cb.count('j'), 2)
    cl1, cl2 = divmod(cb.count('k'), 2)
    cx *= -1 ** ((cm1 + cn1 + cl1) % 2)
    cb = cm2 * 'i' + cn2 * 'j' + cl2 * 'k'
    if len(cb) == 0:
        cz = 'YES'
    elif len(cb) == 3 and cx == -1:
        cz = 'YES'
    else:
        cz = 'NO'

    print("Case #{}: {}".format(i, cz))
