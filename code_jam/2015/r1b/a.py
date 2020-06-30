def f(fa):
    #
    if fa == 2:
        return 10
    else:
        return f(fa - 1) + int('9'*((fa-1)/2)) + int('9'*(fa-(fa-1)/2-1)) + 1

for i in range(1, 1 + input()):
    ca = input()
    cz = 0
    if ca % 10 == 0:
        cz += 1
        ca -= 1
    cb = str(ca)
    cd = len(cb)
    cc = cd/2

    if ca <= 10:
        cz += ca
    else:
        cz += f(cd)
        cz += int(cb[cc:]) + int(cb[cc-1::-1])
        if cb[0:cc] == '1'+'0'*(cc-1):
            cz -= 1
    print "Case #{}: {}".format(i, cz)
