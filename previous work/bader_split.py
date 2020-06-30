#!/usr/bin/env python

#read files
a = open('POSCAR','r').readlines()
a = [[y for y in x.strip().split() ] for x in a[5:7]]

b = open('ACF.dat','r').readlines()
b = [ [float(x) for x in y.strip().split() ] for y in b[2:-4]]
c = []
jj = 0
for i,j in enumerate(a[1]):
    for ii in range(int(j)):
        c.append([a[0][i],b[jj][3],b[jj][4]])
        jj=jj+1
c.sort()


temp = []
chg = []
for i in c:
    if i[0] in ["Ti", "O"]:
        if temp == []:
            temp = i
            chg.append(i[1])
        elif  abs(i[1] - temp[1]) > 0.5:
            print temp[0],len(chg),sum(chg)/len(chg)
            temp = i
            chg = []
            chg.append(i[2])
        else:
            chg.append(i[2])
    else:
        print i[0],i[2] 
print temp[0],len(chg),sum(chg)/len(chg)