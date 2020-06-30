import math

def dis(x,y):
    return math.sqrt((x[1]-y[1])**2 +(x[2]-y[2])**2)

def transfer(x,i,j):
    global afile, bfile
    return x * float(afile[i][j]) / float(bfile[i][j])

def pickAtom(a,b,c):
    return transfer(a[1] - b[1],2,0)+ c[1], transfer(a[2] - b[2],3,1) + c[2], transfer(a[3] - b[3],4,2) + c[3]

co = []
coa = []
cob = []
ele = {}
ele1 = []
ele2 = []
fixlimit = 0.25
k = 0

afile = open('POSCAR_CH4','r').readlines()
afile = [[x for x in y.strip().split() if x != ''] for y in afile]
bfile = open(r'3l','r').readlines()
bfile = [[x for x in y.strip().split() if x != ''] for y in bfile]
for i in range(len(bfile[5])):
    for j in range(int(bfile[6][i])):
        cob.append([bfile[5][i],float(bfile[9+k][0]),float(bfile[9+k][1]),float(bfile[9+k][2])])
        if dis(cob[-1],[0,0.464987,0.166667]) < 0.1 and cob[-1][0] == "O":
            rb = k
        k += 1
k=0
# print len(cob)

for i in range(len(afile[5])-1):
    for j in range(int(afile[6][i])):
        co.append([afile[5][i],float(afile[9+k][0]),float(afile[9+k][1]),float(afile[9+k][2])])
        if dis(co[-1],[0,0.464987,0.166667]) < 0.1 and co[-1][0] == "O":
            ra = k
        k += 1
k = 0
# for i in range(5):
#     print co[i]
# print co[:5], cob[:5]

for i in range(len(co)):
    if co[i][0] not in ["Ti", "O"]:
        ca,cb,cc = pickAtom(co[i],co[ra],cob[rb])
        coa.append([co[i][0],ca,cb,cc])
ca,cb,cc = pickAtom(co[-1],co[ra],cob[rb])
coa += [[co[-1][0],ca,cb,cc]] + cob[:]
# print coa[:4]

for i in range(len(coa)):
    if coa[i][0] in ele.keys():
        ele[coa[i][0]] += 1
    else:
        ele[coa[i][0]] = 1

eleItem = ele.items()
eleItem.sort()
for i,j in eleItem:
    ele1.append(i)
    ele2.append(j)

for i in range(5):
    print ' ' .join(bfile[i])
for i in ele1:
    print i,
print 
for i in ele2:
    print i,
print
print ' '.join(bfile[7])
print ' '.join(bfile[8])
for i in range(len(coa)):
    print '{:12.8f}  {:12.8f}  {:12.8f}'.format(coa[i][1],coa[i][2],coa[i][3]),
    #print coa[1],coa[2],coa[3],
    if coa[i][3] > fixlimit:
        print '  T  T  T'
    else:
        print '  F  F  F'

# print ra, rb, cob[rb]
