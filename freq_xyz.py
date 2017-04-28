ca = open("./OUTCAR", "r").readlines()
ca = [[x for x in y.strip().split() if x != ''] for y in ca]

cs1 = 0
Natom = 0
cb = 0
for ci in ca:
    if ci == []:
        continue
    cc = len(ci)
    if cc == 1 and ci[0][0] == "-":
        cs1 = 0
    if cs1 == 1:
        Natom += 1

    if ci == ["position", "of", "ions", "in", "cartesian", "coordinates", "(Angst):"]:
        cs1 = 1
    if cc > 2 and (ci[1] == "f" or ci[1] == "f/i="):
        print Natom
        cs1 = 2
    if cs1 == 2 and ci[0][0] != "X":
        print ' '.join(ci)
        cb += 1
        if cb > Natom:
            cs1 = 0
            cb = 0
