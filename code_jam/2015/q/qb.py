for i in range(1, 1 + input()):
    ca = input()
    ca = map(int, raw_input().split())
    cz = 0

    while True:
        ca.sort()
        cb = max(ca)
        cc = int(cb/2)
        cd = ca.count(cb)
        if cb > cd + max(cc, cb - cc):
            ca = cd * [cc, cb - cc] + ca[:-cd]
            cz += 1
        else:
            cz += cb
            break

    print("Case #{}: {}".format(i, cz))

