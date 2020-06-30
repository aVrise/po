import numpy as np

a=open("data",'r').readlines()
a=[[ x.strip() for x in y.strip().split() if x != ' ' ] for y in a ]
l=["ptc", "ov", "ova", "cla", "ptd", "sur", "cl"]
data=[]
for i in range(len(l)):
   data.append([])

for i in a:
   if i[0] in l:
      j = l.index(i[0])
      data[j].append(float(i[6]))

data0=np.array(zip(*data))
print len(data0)
for i in range(1,2**len(data0)):
   temp=np.array([0,0,0,0,0,0,0])
   n=[x*int(y) for x,y in enumerate(list(bin(i))[:1:-1]) if y != "0"]
   for j in n:
      temp= temp + data0[j]
   # print i
   if (temp == np.sort(temp)).all() or (temp[::-1] == np.sort(temp)).all():
      print i,n,temp

# print (temp == np.sort(temp)).all() or (temp[::-1] == np.sort(temp)).all()
