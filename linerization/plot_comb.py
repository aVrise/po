import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

a = open('data','r').readlines()
a = [[ float(x) for x in y.strip().split() ] for y in a]
x = [1./3,1./4,1./7,1./9,1./16]

fig = plt.figure()
# fig.set_size_inches(3.5,3.5)
fig.set_size_inches(24/2.55,18/2.55)
ax = fig.add_subplot(111)
ax2 = ax.twinx()
x0 = np.arange(0.,0.41,0.01)
colorList = ['#070707','#B5D99C', '#F9564F', '#F3C677', '#4D7298', '#B8B3E9', '#8DDBE0', '#bebebe', '#D15700', '#EA638C' ,'#00A8E0', 'k', 'k', 'k', 'k', 'k', 'k'] #Black, Green, Red, Yellow, Blue, Purple, cyan, grey, brown, pink, deep sky blue
mks = ['.', 'x', '+', '1', '2', '3', '4']
mks = ['o', '<', '>', 'D', 's', 'P', 'X']
lbs = ['$E_{ads}$', '$E_{a}$', '$E_{r}$', '$E_{b}$', '$E_{des}$', '$E_{v}$']

xx=0
for i in range(len(a[:-1])):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,a[i])
    y0 = slope * x0 + intercept

    if xx == 0:
        xx = ax.plot(x,a[i],marker=mks[i],color=colorList[i],label=lbs[i],linestyle='')
    else:
        xx = xx + ax.plot(x,a[i],marker=mks[i],color=colorList[i],label=lbs[i],linestyle='')
    # plt.plot(x,a,'bx')
    ax.plot(x0,y0,color=colorList[i],lw=1)
    # ax.plot(x0,[a[-1]]*len(x0),'k')
    # plt.plot(-0.33,a[-1],'kx')
    # np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
    # locs, labels = plt.yticks()
    # locs.set_printoptions(formatter={'float': '{: 0.3f}'.format})MultipleLocator(0.01)
    # ax.yaxis.set_major_locator(MultipleLocator(0.15))
    # print(r_value**2)

slope, intercept, r_value, p_value, std_err = stats.linregress(x,a[-1])
y0 = slope * x0 + intercept
xx = xx + ax2.plot(x,a[5],marker=mks[5],color=colorList[7],label=lbs[5],linestyle='')
ax2.plot(x0,y0,color=colorList[7],lw=2, linestyle=':')

ax.set_xlabel(r'$\theta$ / ML',labelpad=12, size=22)


# ax.set_yticks(size=12)
# ax.set_title('',fontsize=20)
ax.tick_params(labelsize=18)
ax2.tick_params(axis='y', labelsize=18)
ax.set_ylabel('Energy / eV', labelpad=8,size=22)
# ax.set_xticklabels(ax.get_xticklabels(), fontsize=18)
# tt = [ x for x in ax.get_yticks()]
# print(tt)
# ax.set_yticklabels(tt, fontsize=18)
# ax.legend(frameon=False)
# ax2.set_yticks(size=12)
ax2.set_ylabel('Energy / eV', labelpad=8,size=22)
xxl = [x.get_label() for x in xx]
plt.legend(xx, xxl, frameon=True, loc='lower right', fontsize=14)
plt.xlim(x0[0],x0[-1])
# plt.xticks(fontsize=12)
# print(r_value**2)
# print a[-1]-intercept,(a[-1]-intercept)/a[-1], r_value**2
# print "y =",slope,"x +",intercept,r_value**2, a[-1]-intercept, slope/(a[-1]-intercept)

# plt.show()
plt.savefig('../out/fig2.png', transparent = False, dpi = 300,pad_inches=0,bbox_inches='tight')
