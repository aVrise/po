'''
data structure pattern:
_ #separator
I [energy] # initail/intermediate state energy
T [energy] # transition state energy
C [energy] # compare energy at the same x value
I [energy]
T [energy]
I [energy]
F [energy] # Final state (Not connect with next bar)
_
'''
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as ip
import scipy.optimize as op
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib


def comp(a, b):
    return min(map(lambda x: abs(x - b), a))

def plotText(a, b, c, d, e):
    global text_coor, text_limit
    if comp(text_coor[int(a/ll)], c - b) > text_limit or d: 
        ax.text(a + 0.5 * ll, c - b, '{:04.2f}'.format(c - b),
                horizontalalignment='center', verticalalignment='bottom', fontsize=FontSize, color = e)
        if not d:
            text_coor[int(a/ll)].append(c - b)

def Ddash(d1, d2, d3, d4, d5):
    global ll, FontSize
    # draw dashed line between 0 and 0
    # ax.plot([d1, d1 + ll], [d3 - d2, d4 - d2], '{}--'.format(d5), color = d5, lw=1)
    ax.plot([d1, d1 + ll], [d3 - d2, d4 - d2], linestyle = '--', color = d5, lw=1)   
    return d1 + ll

def Dcurve(d1, d2, d3, d4, d5, d6):
    # draw curve of transition state
    global ll, FontSize
    y1 = d3 - d2
    y2 = d4 - d2
    y3 = d5 - d2
    if y2<y3 or y2<y1:
        ax.plot([d1, d1 + ll], [y1, y3], color = d6, lw=1,linestyle = '--',)
        return d1 + ll   
    vert = [(d1, y1), (d1 + 0.3 * ll, y2), (d1 + 0.44 * ll, y2), (d1 + 0.5 *
                                                                  ll, y2), (d1 + 0.56 * ll, y2), (d1 + 0.7 * ll, y2), (d1 + ll, y3)]
    code = [Path.MOVETO, Path.CURVE4, Path.CURVE4,
            Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    path = Path(vert, code)
    patch = patches.PathPatch(path, facecolor='none', lw=1, edgecolor = d6)
    ax.add_patch(patch)
    plotText(d1, d2, d4, 0, d6)
    return d1 + ll

def Dline(d1, d2, d3, d4):
    global ll, FontSize
    # draw line of current data
    ax.plot([d1, d1 + ll], [d3 - d2, d3 - d2], color = d4, lw=2)
    plotText(d1, d2, d3, 0, d4) # Always display the value of bar set the fourth parameter true, vice versa.
    return d1 + ll

ll = 0.5
FontSize = 12
text_limit = 0.5 # set the limit between text and upper text
colorList = ['k', 'k', 'k', 'g', 'g', 'g', 'b', 'r', 'k', 'k']
# colorList = ['#070707']+['#89BD9E']
# colorList = ['#070707', '#89BD9E', '#F9564F', '#F3C677', '#4D7298', '#B8B3E9', '#8DDBE0', 'r', 'k', 'k'] #Black, Green, Red, Yellow, Blue, Purple, cyan
# text_coor = [[1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000],
            #  [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000]]
# dat2 = dat.copy()
fig = plt.figure()
fig.set_size_inches(6,8)
# fig.set_size_inches(8,6)
SameStartYValue=True

a = open(r'data', 'r').readlines()
a = [x.strip().split() for x in a]

# print a

#get the index of __
i=0
b=[i for i,j in enumerate(a) if j[0]=='__']
c=[311,312,313]

# plot lines       
for ia in range(0,len(b)-1):
    ax = fig.add_subplot(c[ia], xticks = [])
    numOfUs = -1
    numOfEle = []
    maxEle = 0
    dat = []
    text_coor = [[1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000],
             [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000], [1000]]
    for i in a[b[ia]+1:b[ia+1]]:
        if i[0] == '_':
            numOfUs += 1
            dat.append([])
            numOfEle.append(-1)
        elif i[0] in ['I', 'i', 'T', 't', 'F', 'f', 'C', 'c']:
            numOfEle[numOfUs] += 1
            dat[numOfUs].append([])
            if i[0] in ['I', 'i']:
                dat[numOfUs][numOfEle[numOfUs]].append(0)
            elif i[0] in ['T', 't']:
                dat[numOfUs][numOfEle[numOfUs]].append(1)
            elif i[0] in ['F', 'f']:
                dat[numOfUs][numOfEle[numOfUs]].append(2)
            elif i[0] in ['C', 'c']:
                dat[numOfUs][numOfEle[numOfUs]].append(3)
            dat[numOfUs][numOfEle[numOfUs]].append(float(i[1]))
        else:
            raise RuntimeError('The data file is written invalidly.')
        maxEle = max(maxEle, numOfEle[numOfUs])
    dat.pop()
    numOfEle.pop()
    maxEle = (maxEle + 2) / 2
    # print dat,numOfEle,numOfUs

    for i in range(numOfUs):
        # axe
        FirstPoint = 1
        x0 = 0.0
        if SameStartYValue == True:
            yc = dat[0][0][1]   
        else:
            yc = dat[i][0][1]
        for j in range(numOfEle[i] + 1):
            if FirstPoint == 0:
                if dat[i][j][0] == 1:
                    x0 = Dcurve(x0, yc, dat[i][j - 1][1],
                                dat[i][j][1], dat[i][j + 1][1], colorList[i])
                    FirstPoint = 1
                    continue
                elif dat[i][j][0] in [0, 2] and dat[i][j - 1][0] not in [1, 2, 3]:
                    x0 = Ddash(x0, yc, dat[i][j - 1][1],
                            dat[i][j][1], colorList[i])
                elif dat[i][j - 1][0] == 3:
                    x0 -= ll
                else:
                    x0 += ll * 2
            x0 = Dline(x0, yc, dat[i][j][1], colorList[i])
            FirstPoint = 0
    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    plt.axis([xmin-0.1*xmax, xmax+0.1*xmax, ymin-0.1*ymax, 1.2 * ymax])
    # plt.yticks(range(int(ymin),int(ymax)+1))
    plt.ylabel('Energy ('+a[b[ia]][1]+' V) / eV',labelpad=18,fontsize=12)
    plt.yticks(fontSize=12)
# plt.ylabel('Energy ('+a[b[ia]][1]+' V) / eV',labelpad=5)
# ytick = np.arange(-4,4,0.02)
# for i in range(1, maxEle):
#     xtick.append('{}H'.format(i))
plt.xlabel('Reaction Coordinate',labelpad=14,fontsize=16)
# plt.xticks([])
# fig.ylabel('XX')

# plt.xticks(fontSize=14)
# plt.xticks(np.arange(0.25, 1. * maxEle+0.25, 1.), ([r'$CH*$',r'$CH_2*$',r'$CH_3*$',r'$CH_4*$',r'$Product$']))
# plt.xticks(np.arange(0.25, 1. * maxEle+0.25, 1.), ([r'$CHOH*$',r'$\frac{CH*}{CH_2OH*}$',r'$CH_2*$',r'$CH_3*$',r'$CH_4*$']))
# plt.xticks(np.arange(0.25, 1. * maxEle+0.25, 1.), ([r'$CH_2O$',r'$CH_2OH*$'+'\n'+'${CH_3O*}$',r'${CH_3OH*}$'+'\n'+'${CH_4*}$']),fontsize=14)
# plt.xticks(np.arange(0.25, 1. * maxEle + 0.25, 1.),([r'$(P)CO$', r'$CO_2(V)$']),fontSize=14)
# plt.xticks(np.arange(0.25, 1. * maxEle + 0.25, 1.), ([r'$3Hs$',r'$4Hs$']))
# plt.xticks(np.arange(0.25, 0.7 * maxEle + 0.25, 1.), ([r'$CO*$',r'$1H$',r'$2Hs$',r'$3Hs$']))
# plt.xticks(np.arange(0.25, 1. * maxEle + 0.25, 1.), ([r'$CH_2OH*$' +'\n'+r'$CH_3O*$',r'$CH_3OH*$'+'\n'+r'$(P)CH_4$']))
# plt.xticks(np.arange(0.25, 1. * maxEle + 0.2, 1.),([r'$CO_2(H)*$', r'$CO_2(V)*$', r'$CO*$']))
# plt.xticks(np.arange(0.25, 1. * maxEle + 0.25, 1.),([r'$CO*$', r'$CHO*$', r'$CHOH*$', r'$CH_2OH*$']))
# plt.xticks(np.arange(0.25, 1.1 * maxEle + 0.25, 1.),([r'$CO*$', r'$CHO*$', r'$CH_2O*$', r'$CH_3O*$']))
# plt.xticks(np.arange(0.25, 1. * maxEle + 0.26, 1.),([r'$CO$', r'$CO*$', r'$1H$', r'$2Hs$', r'$3Hs$', r'$4Hs$', r'$Products$']))
plt.xticks(np.arange(0.25, 1. * maxEle+0.25, 1.), ([r'$CH_2OH*$',r'$CH_2*$',r'$CH_3*$',r'$CH_4$']),fontsize=14)
# plt.xticks(np.arange(0.25, 1. * maxEle + 0.25, 1.), ([r'$CO*$',r'$COH*$'+'\n'+r'$CHO*$',r'$CHOH*$'+'\n'+r'$CH_2O*$',r'$CH_2OH*$'+'\n'+r'$CH_3O*$']))
# plt.xticks(np.arange(0.25, 1. * maxEle + 0.25, 1.), ([r'$CO*$',r'$CHO*$',r'$CH_2O*$',r'$ CH_2OH*$'+'\n'+ r'$CH_3O*$']))
# plt.xticks(np.arange(0.25, 1. * maxEle + 0.25, 1.), ([r'$CO$',r'$CO*$',r'$CO_2*$',r'$CO_2$']))


# plt.axis([xmin-0.1*xmax, xmax+0.1*xmax, -2, 4])
# plt.legend([1,2])
# matplotlib.rcParams.update({'font.size': 120})
# plt.rcParams['figure.figsize']=(4,4)
plt.savefig('lpb_deo_hr.tiff', transparent = True, dpi = 1000,pad_inches=0,bbox_inches='tight')
# plt.show()
