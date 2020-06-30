#!/usr/bin/env python
import matplotlib
#matplotlib.use("Agg")
matplotlib.use("Pdf")
from matplotlib import cm, colors
import matplotlib.pyplot as plt
import numpy as np
import sys

#
if len(sys.argv) == 2:
    sys.argv = sys.argv + [0,0]
elif len(sys.argv) == 3:
    sys.argv = sys.argv + [0]

#Colormap_STM        
STM = np.arange(0,348,1)
STM = np.array([STM, STM - 127, STM * 2 - 508]).T/255.
STM[STM < 0] = 0
STM[STM > 1] = 1
# cmap = cm.coolwarm
cmap = colors.ListedColormap(STM)

#Convert data file to X, Y, Z
a = open('./{}'.format(sys.argv[1]), "r").readlines()
a = [[ float(x) for x in u.strip().split() if x != '' ] for u in a[1:] ]
u = lambda i: reduce(lambda s, z: [[],s[1] + [s[0]]] if z == [] else [s[0] + [z[i]], s[1]], a, [[],[]])[1]
X, Y, Z = np.array(map(u, range(3)))

#Expend X, Y, Z
nrow = 1 if sys.argv[2] == 0 else int(sys.argv[2])
ncol = int(np.round(np.amax(Y) / np.amax(X)) * nrow)
Z = np.kron(np.ones((nrow,ncol)), Z)
X = np.kron(np.ones((nrow,1)), reduce(lambda i, j: np.insert((i.T + np.amax(X, axis=1)).T, 0, X.T, axis=1), range(ncol - 1), X))
Y = np.kron(np.ones(ncol), reduce(lambda i, j: np.insert(i + np.amax(Y, axis=0) ,0, Y, axis=0), range(nrow - 1), Y))

# Levels 
resolution = 0.01 if sys.argv[3] == 0 else  float(sys.argv[3])
levels = np.arange(np.amin(Z), np.amax(Z) + resolution, resolution) 

# Plot
plt.clf()
plt.contourf(X, Y, Z, levels, cmap=cm.get_cmap(cmap, len(levels) - 1))

#Miscellaneous
delta = int(np.ceil(nrow/5.))
plt.axis('scaled')
plt.axis('off')
plt.annotate('', xy=(delta, delta), xytext=(delta * 11, delta), arrowprops=dict(arrowstyle = "-", color = '1', connectionstyle = "bar,fraction = -0.05"))
plt.text(delta, delta, '{:d} nm'.format(delta),color = '1')

#cax = plt.axes()
#plt.title('Filled contours')
#plt.colorbar(cax)

#plt.gcf().set_size_inches(np.amax(X), np.amax(Y))
plt.savefig('./stm.png', transparent = True, dpi = 300)
#plt.show()
