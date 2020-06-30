import numpy as np

a = open(r'POS1','r').readlines()
a = [[ y for y in x.strip().split() if y != ' ' ] for x in a ]

cell = [[ float(y) for y in x] for x in a[2:5]]
cell = np.array(cell)

ele = [x for x in a[5]]
num = {}
for i in range(len(ele)) :
    num[ele[i]]=int(a[6][i])

coord = []
coord_starter = 9
for ii,ij in enumerate(ele):
    coord.append([])
    for j in range(num[ij]):
        coord[ii].append([ float(x) for x in a[coord_starter][0:3]])
        coord_starter=coord_starter+1

distance=[]
ex_array=np.array([[1.,0.,0.],[0.,0.,0.,],[0.,1.,0.],[-1.,-0. ,-0.],[-0., -1., -0.],[ 1.,  1.,  0.],[ 1., -1. , 0.],[-1.,  1. , 0.],[-1., -1., -0.]])
for i in np.array(coord[0][0]):
    for j in np.array(coord[1][0]):
        distance.append(np.min(np.linalg.norm(np.dot(i-j+ex_array,cell),axis=1)))



print distance[0:10]
