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

colorList = ['#070707', '#F9564F','#89BD9E',  '#F3C677', '#4D7298', '#B8B3E9', '#8DDBE0'] #Black, Red, Green, Yellow, Blue, Purple, cyan
sub=[312,313]
sht=7.34125
lgd=['0.1 e','0.3 e','0.5 e','0.7 e','0.9 e']
img=mpimg.imread('psur.png','r')
fig = plt.figure()
fig.set_size_inches(8,10)
plt.subplots_adjust(hspace=0.05)
ft=25
fts=20

# plot img of slab

p1 = plt.subplot(311)
p1.imshow(img)
plt.xticks([])
plt.yticks([])

p2 = plt.subplot(312)

a=open('bader_psur','r').readlines() #bader_psur Fresh	a	0	0.01	0.1	0.3	0.5	0.7	0.9
a=np.array([[float(y) for y in x.strip().split()] for x in a if x.strip() != ('' or '\t')])
bader_psur=["Fresh","V/C","S/C","0.01 e","0.1 e","0.3 e","0.5 e","0.7 e","0.9 e"]
k=(1-0.531069)/180
bader_psur_corr=[0, 0, 0, 0.01*k, 0.1*k, 0.3*k, 0.5*k, 0.7*k, 0.9*k]
# print len(a[0])
# for i,j in enumerate(a[:,0]):
#     if j + sht > 31.6572:
#         a[i,0]=j+sht-31.6572
#     else:
#         a[i,0]=j+sht

# plt.xlim([0,31.6572])
plt.xlim([0,36.6572])
plt.xticks([])
plt.yticks([6.92,6.96,7.00,7.04,7.08],fontsize=fts)

plt.ylabel(r"$\bar{q}_O \ / \ e$", fontsize=ft,labelpad=fts)
for i,j in enumerate([1,2,4,6,8]):
    p2.plot(a[0:20,0],a[0:20,j+1]-bader_psur_corr[j],'-o',color=colorList[i],linewidth=1,markersize=3)

p3 = plt.subplot(313)

# for i,j in enumerate(a[:,0]):
#     if j + sht > 31.6572:
#         a[i,0]=j+sht-31.6572
#     else:
#         a[i,0]=j+sht

# plt.xlim([0,31.6572])
plt.xlim([0,36.6572])
plt.xticks([])
plt.yticks(fontsize=fts)

plt.ylabel(r"$\bar{q}_{Ti} \ / \ e$", fontsize=ft,labelpad=fts)
for i,j in enumerate([1,2,4,6,8]):
    p3.plot(a[20:,0],a[20:,j+1]-bader_psur_corr[j],'-o',color=colorList[i],linewidth=1,markersize=3,label=bader_psur[j])
plt.yticks([1.93,1.94,1.95,1.96,1.97,1.98,1.99],fontsize=fts)


# plt.legend(frameon=False,fontsize=fts)
plt.xlabel("z values",fontsize=ft,labelpad=fts*2)
# for i in range(len(a[0,:])-1):
#     print (a[:,i+1]-bader_psur_corr[i]).sum()*6
# print bader_psur_corr
# plt.show()
plt.savefig('bader_paper_hr.tiff',dpi=1000, pad_inches=0,bbox_inches='tight',transparent=True)