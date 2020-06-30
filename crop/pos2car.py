#!/Users/jy/anaconda3/bin/python
import sys
import numpy as np

input_file=open(sys.argv[1],'r').readlines()
input_file=[[ x for x in y.strip().split() ] for y in input_file ]

vector_x=np.array([float(x) for x in input_file[2]])
vector_y=np.array([float(x) for x in input_file[3]])
vector_z=np.array([float(x) for x in input_file[4]])

a = np.linalg.norm(vector_x)
b = np.linalg.norm(vector_y)
c = np.linalg.norm(vector_z)
alpha = np.arccos(vector_x.dot(vector_z)/a/c) * 360/2/np.pi
beta = np.arccos(vector_y.dot(vector_z)/b/c)* 360/2/np.pi
gamma = np.arccos(vector_x.dot(vector_y)/a/b) * 360/2/np.pi

print("!BIOSYM archive 3\nPBC=ON\nCOMMENT\n!DATE")
print ("{}{:10.4f}{:10.4f}{:10.4f}{:10.4f}{:10.4f}{:10.4f}{}".format("PBC",a, b, c, alpha, beta, gamma," (P 1)"))

ele={}
for i in range(len(input_file[5])):
    ele[input_file[5][i]] = int(input_file[6][i]) 

lines=9
coor=[]
nele=-1
for i in ele.keys():
    nele = nele + 1
    coor.append([])
    for j in range(ele[i]):
        k = np.array([float(x) for x in input_file[lines+j][:3]]).dot(np.vstack([vector_x,vector_y,vector_z]))
        print("{:<5s}{:15.9f}{:15.9f}{:15.9f}{:>23s}".format(i,k[0],k[1],k[2],i))
    lines = lines + ele[i]
print("end\nend")


awk '{for(i=1;i<=NF;i++){a[(NR-NR%250)/250,FNR,i]=$i}}END{for(j=1;j<=FNR;j++){printf "%s ",a[0,j,1];for(k=2;k<=NF;k++){b=0;for(i=0;i<=(NR/250);i++){b+=a[i,j,k]};printf "%s ",b;}print ""}}' t{1..12} > tt
awk '{for(i=1;i<=NF;i++){a[(NR-NR%250)/250,FNR,i]=$i}}END{for(j=1;j<=FNR;j++){printf "%s ",a[0,j,1];b=0;for(i=0;i<=(NR/250);i++){printf "%s ",a[i,j,8];b+=a[i,j,8]};printf "%s\n",b/12}}' t{1..12} > ttt

awk '{for(i=1;i<=NF;i++){a[(NR-NR%300)/300,FNR,i]=$i}}END{for(j=1;j<=FNR;j++){printf "%s ",a[0,j,1];b=0;for(i=0;i<=(NR/300);i++){printf "%s ",a[i,j,8];b+=a[i,j,8]};printf "%s\n",b/12}}' t{1..12} > ttt
awk '{for(i=1;i<=NF;i++){a[NR%2001,FNR,i]=$i}}' DOS49 