#!/usr/bin/env python

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import sys


def f(x):
    return 0.2*x-0.1

def g(x):
    if x>=7.87399 and x<=27.6273:
        return 1
    else:
        return 0
# constant

colorList = ['#070707', '#89BD9E', '#F9564F', '#F3C677', '#4D7298', '#B8B3E9', '#8DDBE0'] #Black, Green, Red, Yellow, Blue, Purple, cyan
sub=[312,313]
sht=7.34125
lgd=['0.1 e','0.3 e','0.5 e','0.7 e','0.9 e']
img=mpimg.imread('psur.png','r')
fig = plt.figure()
fig.set_size_inches(18.3286,18.3286/16*9)
plt.subplots_adjust(hspace=0.05)
ft=25
fts=15

# plot img of slab

# p1 = plt.subplot(311)
# p1.imshow(img)
# plt.xticks([])
# plt.yticks([])


# plot chg_diff
# p2 = plt.subplot(313)
a=open(sys.argv[1],'r').readlines()
a=np.array([[float(y) for y in x.strip().split()] for x in a if x.strip() != ('' or '\t')])


# for i,j in enumerate(a[:,0]):
#     if j + sht > 31.6572:
#         a[i,0]=j+sht-31.6572
#     else:
#         a[i,0]=j+sht


plt.xlim([0,36.6572])
plt.xticks([])
plt.yticks(fontsize=fts)
plt.ylabel(r"$\Delta {\rho (z)} \ /\  e \cdot  \mathrm{\AA}^{-1}$", fontsize=ft, labelpad=fts*2)
# k=(1-0.531069)/480
# bader_psur_corr=[0,  0.1*k, 0.3*k, 0.5*k, 0.7*k, 0.9*k]
for i in range(1,len(a[0])):
    # b = [(a(ii,i) - f(i)*g(a[ii,0]))/len(a[:,0]) for ii in range(len(a[:,0]))]
    b = map(lambda x,y: np.array((y-f(i)*g(x))/len(a[:,0])),a[:,0],a[:,i])
    plt.plot(a[:,0],b,color=colorList[i],linewidth=2)
    # plt.plot(a[:,0],a[:,i]/len(a[:,0]),color=colorList[i],linewidth=2)
    # print i,sum(a[:,i])

plt.plot(a[:,0],[0.00020/480]*len(a[:,0]),'k')

# plot bader diff

# p3 = plt.subplot(312)

# a=open(sys.argv[2],'r').readlines() #bader_psur Fresh	a	0	0.01	0.1	0.3	0.5	0.7	0.9
# a=np.array([[float(y) for y in x.strip().split()] for x in a if x.strip() != ('' or '\t')])
# bader_psur=["Fresh","vac","sol","0.01 e","0.1 e","0.3 e","0.5 e","0.7 e","0.9 e"]
# print len(a[0])
# # for i,j in enumerate(a[:,0]):
# #     if j + sht > 31.6572:
# #         a[i,0]=j+sht-31.6572
# #     else:
# #         a[i,0]=j+sht

# # plt.xlim([0,31.6572])
# plt.xlim([0,36.6572])
# plt.xticks([])
# plt.yticks(fontsize=fts)


# plt.ylabel(r"$\Delta \bar{q} \ / \ e$", fontsize=ft,labelpad=fts)
# for i,j in enumerate([1,2,4,6,8]):
#     p3.plot(a[:,0],a[:,j+1],'-o',color=colorList[i],linewidth=2,label=bader_psur[j])

plt.legend(lgd,fontsize=fts,frameon=False,loc=3)
plt.xlabel("z values",fontsize=ft,labelpad=fts*2)
# plt.show()
plt.savefig('chg_paper_hr.png',dpi=1000, pad_inches=0,bbox_inches='tight',transparent=True)