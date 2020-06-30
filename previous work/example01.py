'''
Test combinations of contouring, filled contouring, and image plotting.
For contour labelling, see contour_demo.py.

The emphasis in this demo is on showing how to make contours register
correctly on images, and on how to get both of them oriented as
desired.  In particular, note the usage of the "origin" and "extent"
keyword arguments to imshow and contour.
'''
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import mlab, cm, colors

# Default delta is large because that makes it fast, and it illustrates
# the correct registration between image and contours.

#extent = (-8, 10, -10, 10)

x = np.arange(-2., 3., 1.)
y = np.arange(-2., 3., 1.)
X, Y = np.meshgrid(x, y)
z1 = np.array([-1, 0, 1, 0, -1])
z1, z2 = np.meshgrid(z1, z1.T)
Z = z1 + z2

STM = np.arange(0,348,1)
STM = np.array([STM, STM - 127, STM * 2 - 508]).T/255.
STM[STM < 0] = 0
STM[STM > 1] = 1
STM = STM

resolution = 0.01

levels = np.arange(np.amin(Z), np.amax(Z) + resolution, resolution) # Boost the upper limit to avoid truncation errors.

#norm = cm.colors.Normalize(vmax=abs(Z).max(), vmin=-abs(Z).max())
#cmap = cm.coolwarm
cmap = colors.ListedColormap(STM)
print cmap

cset1 = plt.contourf(X, Y, Z, levels, cmap=cm.get_cmap(cmap, len(levels) - 1))

plt.title('Filled contours')
plt.colorbar(cset1)

plt.show()
#print STM
