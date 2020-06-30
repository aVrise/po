#!/usr/bin/env python

ca = open("POSCAR", "r").readlines()
Nkele = [x for x in ca[5].strip().split() if x != '']
ca = [int(x) for x in ca[6].strip().split() if x != '']
Nele = []
for ci, cj in enumerate(ca):
    Nele += cj * [Nkele[ci]]
Natom = sum(ca)

ca = open("OUTCAR", "r").readlines()
ca = [[x for x in y.strip().split() if x != ''] for y in ca]

cs1 = 0
cb = 0
for ci in ca:
    if len(ci) < 5:
        continue
    if ci[1] == "f" or ci[1] == "f/i=":
        print Natom
        cs1 = 2
    if cs1 == 2 and ci[0][0] != "X":
        if cb > 0:
            print Nele[cb - 1],
        print ' '.join(ci)
        cb += 1
        if cb > Natom:
            cs1 = 0
            cb = 0
