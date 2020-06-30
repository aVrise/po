#!/Users/jy/anaconda3/bin/python
import sys
import numpy as np

e=3E-2
def period(x, y):
    z = 5E-2
    if (abs(x[0]-y[0])%1 < z or abs(x[0]-y[0])%1 > 1 - z) and (abs(x[1]-y[1])%1 < z  or abs(x[1]-y[1])%1 > 1 - z) and (abs(x[2]-y[2])%1 < z or abs(x[2]-y[2])%1 > 1 - z):
        return True


def expend(x):
    return x + np.array([[-1.,1.,0.],[-1.,0.,0.],[-1.,-1.,0.],[0.,1.,0.],[0.,0.,0.],[0.,-1.,0.],[1.,1.,0.],[1.,0.,0.],[1.,-1.,0.]])

def uniq(x):
    z = []
    if len(x) < 2:
        return x
    for i in range(len(x)):
        for j in x[i+1:]:
            if period(x[i],j):
                z.append(i)
                break
    return np.delete(x,z,axis=0)

    

# read POSCAR of 16n
input_file=open(sys.argv[1],'r').readlines()
input_file=[[ x for x in y.strip().split() ] for y in input_file ]
vector_x=np.array([float(input_file[2][0]),float(input_file[3][0]),float(input_file[4][0])])
vector_y=np.array([float(input_file[2][1]),float(input_file[3][1]),float(input_file[4][1])])
vector_z=np.array([float(input_file[2][2]),float(input_file[3][2]),float(input_file[4][2])])

# vector_x=np.array([float(x) for x in input_file[2]])
# vector_y=np.array([float(x) for x in input_file[3]])
# vector_z=np.array([float(x) for x in input_file[4]])

ele={}
for i in range(len(input_file[5])):
    ele[input_file[5][i]] = int(input_file[6][i]) 

lines=9
coor=[]
nele=-1
for i in ele.keys():
    nele = nele + 1
    coor.append([])
    if str(i) == 'H':
        coor_H=np.array([float(x) for x in input_file[lines][:3]]).dot(np.vstack([vector_x,vector_y,vector_z]).T)
        coor[nele].append([coor_H,input_file[lines][3]])
        lines = lines + 1
        continue
    for j in range(ele[i]):
        for k in expend(np.array([float(x) for x in input_file[lines+j][:3]])):
            coor[nele].append([k.dot(np.vstack([vector_x,vector_y,vector_z]).T),input_file[lines+j][3]])
    lines = lines + ele[i]

unit=np.vstack([vector_x/4,vector_y/4,vector_z]).T
k3 = np.array([[1.,2.,0.],[2.,1.,0.],[0.,0.,1.]]) # kc
k4 = np.array([[2.,0.,0.],[0.,2.,0.],[0.,0.,1.]])
k7 = np.array([[3.,1.,0.],[-1.,2.,0.],[0.,0.,1.]]) # 
k9 = np.array([[3.,0.,0.],[0.,3.,0.],[0.,0.,1.]])
k12 = np.array([[2.,4.,0.],[4.,2.,0.],[0.,0.,1.]]) # kc
k16 = np.array([[4.,0.,0.],[0.,4.,0.],[0.,0.,1.]])
kc = {}
kc["3n"] = kc["12n"] = np.array([[0.,1.,0.],[1.,0.,0.],[0.,0.,1.]])
kc["4n"] = kc["7n"] = kc["9n"] = np.eye(3)
kt = [["3n",k3.dot(unit)],["4n",k4.dot(unit)],["7n",k7.dot(unit)],["9n",k9.dot(unit)],["12n",k12.dot(unit)]]

for i in kt:
    i[1] = i[1].dot(kc[i[0]])
    output=[i[0],"1.0"," ".join([str(x) for x in i[1][0]])," ".join([str(x) for x in i[1][1]])," ".join([str(x) for x in i[1][2]]),"Selective dynamics","Direct"]
    aele={}
    ii = -1
    for j in ele.keys():
        ii = ii + 1
        kk2=[]
        for k in coor[ii]:
            kk=(k[0]-coor_H+np.array([0.,0.,coor_H[2]])).dot(kc[i[0]]).dot(np.linalg.inv(i[1]))
            if kk[:2].max() - 1 > e or kk[:2].min() < -e :
                continue
            else:
                kk2.append(kk.tolist()+[k[1]]*3)
        kk2 = uniq(kk2)
        output = output + ["   ".join(x) for x in [[str(y) for y in z] for z in kk2]]
        aele[j] = len(kk2)
    output.insert(5," ".join([str(x) for x in aele.values()]))
    output.insert(5," ".join([str(x) for x in aele.keys()]))
    
    print("\n".join(output[5:7]))
    print("-----")
    f = open("../out/POSCAR_"+i[0],"w+")
    f.write("\n".join(output))
    f.write("\n")
    f.close()


