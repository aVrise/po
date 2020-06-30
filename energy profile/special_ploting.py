import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as ip
import scipy.optimize as op
from matplotlib.path import Path
import matplotlib.patches as patches
from scipy import interpolate

def plotText(a, b, c, d):
        ax.text(a + 0.5 * ll, c - b, '{:04.2f}'.format(c - b),
                horizontalalignment='center', verticalalignment='bottom', fontsize=FontSize)


def Dline(d1, d2, d3, d4):
    global ll, FontSize
    # draw line of current data
    ax.plot([d1, d1 + ll], [d3 - d2, d3 - d2], d4, lw=2)
    plotText(d1, d2, d3, 1)
    return d1 + 1.5

ll = 0.5
FontSize = 9
numOfUs = -1
numOfEle = []
maxEle = 0
dat = []
colorList = ['k', 'k', 'k', 'k']
text_coor = [[1000], [1000], [1000], [1000], [1000], [1000],
             [1000], [1000], [1000], [1000], [1000], [1000], [1000]]
# dat2 = dat.copy()
fig = plt.figure()
ax = fig.add_subplot(111)

data = [[0.5,-1151.03],
        [0.625,-1150.96],
        [0.75,	-1150.75],
        [0.875,	-1150.57],
        [1.,	-1150.39],
        [1.125,	-1149.98],
        [1.25,	-1149.15],
        [1.375,	-1149.23],
        [1.5,	-1149.29]
]
data1 = np.array(data)
color = {'nearest':'k', 'zero':'r', 'linear':'b', 'quadratic':'g', 'cubic':'c'}
x0 = 0
yc = data[0][1]
x0 = Dline(x0, yc, data[0][1], 'k')
x0 = Dline(x0, yc, data[8][1], 'k')
X=data1.T[0]
Y=data1.T[1]-yc
xnew = np.arange(0.5, 1.5, 0.01)
# tck = interpolate.splrep(data1.T[0], data1.T[1]-yc, s=0,k=1)

# ynew = interpolate.splev(xnew, tck, der=0)

plt.plot(X, Y, 'ko')
plt.plot(xnew, interpolate.interp1d(X, Y, kind='quadratic')(xnew), 'k')
# x=np.arange(0.5, 1.5, 0.01)
# for kind in ['nearest', 'zero', 'linear', 'quadratic', 'cubic']:
#     f = interpolate.interp1d(X, Y, kind=kind)
#     y = f(x)
#     plt.plot(x, y, label=kind, color=color[kind])
# plt.legend(loc=3)
# plt.plot(X, Y, 'o')
xtick = []
for i in range(1, maxEle):
    xtick.append('{}H'.format(i))
plt.ylabel('Energy/eV')
# plt.xticks(np.arange(0.25, 1. * maxEle + 0.25, 1.), (['3Hs','4Hs','5Hs']))
# plt.xticks(np.arange(0.25, 1. * maxEle + 0.25, 1.), (['0H','1H','2Hs','3Hs']))
# plt.xticks(np.arange(0.25, 1. * maxEle + 0.25, 1.),(['1H', '2Hs', '3Hs', '4Hs']))
plt.xticks([0.25,1.75],(['CHOH', 'CH + OH']))
xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
plt.axis([xmin, xmax, ymin, 1.1 * ymax])
# plt.savefig('./c2.png', transparent = True, dpi = 300)
plt.show()