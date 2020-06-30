# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def f(a,b):
    l=len(a)
    for i in range(b):
        t=a[:]+[a[0]]
        a=[]
        for ii in range(l):
            a.append((t[ii]+t[ii+1])/2)
    a=a[-int(b)/2:]+a[:-int(b)/2]  
    return a

def g(a,b):
    l=len(a)
    aa=[]
    for i in range(l):
        bb=0
        for ii in range(b):
            bb=bb+a[(i+ii)%l]
        aa.append(bb/b)
    return aa 
a=open('/Users/jy/Downloads/3','r').readlines()
a=[[float(x) for x in y.strip().split()] for y in a if y != ""]
z=36.6572
x=np.arange(0,z-0.01,z/480)
colorList = ['#070707','#F9564F','#B5D99C',  '#4D7298','#F3C677', '#F9564F', '#B8B3E9','#D15700', '#8DDBE0', '#bebebe',  '#EA638C' ,'#00A8E0', 'k', 'k', 'k', 'k', 'k', 'k'] #Black, Green, Red, Yellow, Blue, Purple, cyan, grey, brown, pink, deep sky blue
llegend=['S/C', '0.1 e', '0.3 e', '0.5 e', '0.7 e', '0.9 e']
y=[3,-12]
# plt.plot([26.1459]*2,y,'k--') #bridging O

for j in [0, 3, 5]:
    plt.plot(x[345:380],f(a[j],30)[345:380],color=colorList[j],label=llegend[j],linewidth=2)
    # plt.plot(x[232:400],f(a[j],30)[232:400],color=colorList[j],label=llegend[j],linewidth=2)

# for i in [2,10,20,30,40,50]:
#     plt.plot(x,g(a[1],i))

# plt.plot(x[232:400],a1[232:400])
plt.legend(frameon=False,fontsize=12,loc=4)
plt.ylabel("(x,y) average potential / V",fontsize=18)
plt.xlabel("z values / $\AA$",fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
# plt.show()

plt.savefig('test30p.tiff', transparent = True, dpi = 300, pad_inches=0, bbox_inches='tight')
