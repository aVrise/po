import re

for i in range(1, 1 + input()):
    ca = raw_input()
    cb = ca
    for ci in range(10):
        cb = re.sub(''+str(ci)+'+', str(ci), cb)

    ci = 0
    if len(cb) == 1:
        cz = ca
        print("Case #{}: {}".format(i, cz))
        continue
    while ci < len(cb) - 1:
        if int(cb[ci]) > int(cb[ci + 1]):
            ci = cb[ci]
            break
        ci += 1
    else:
        cz = ca
        print("Case #{}: {}".format(i, cz))
        continue
    ci = ca.index(ci)
    if ci == 0:
        cz = str(int(ca[0]) - 1) + (len(ca) - 1) * '9'
    else:
        cz = ca[:ci] + str(int(ca[ci]) - 1) + (len(ca) - ci - 1) * '9'
    print("Case #{}: {}".format(i, int(cz)))
