import numpy as np
import matplotlib
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt

def drawRing(numOfRings, numOfLayers, patches):
    global rad
    angleApp = 360./numOfRings
    starter = -angleApp/2
    for i in range(numOfRings):
        patches += [Wedge((0., 0.), rad*(numOfLayers+1),starter,starter+angleApp,width=rad)]
        starter += angleApp

def ts(a, layers):
    if a == 3*2**layers:
        return 0
    return a

def cavg(a,b):
    m = max((a[0]+b[0]), (a[1]+b[1]), (a[2]+b[2]))
    return [[(a[0]+b[0])/m, (a[1]+b[1])/m, (a[2]+b[2])/m]]

def colorsApp(index, layers, list):
    # print list
    list[layers+1] += [list[layers][index]]
    list[layers+1] += cavg(list[layers][index],list[layers][ts(index+1,layers)])

fig, ax = plt.subplots()

patches = []
N = 4 # the number of rings
rad = 1
r = [[1.,0.,0.],[220./256,76./256,70./256],[228./256,36./256,35./256]]
g = [[0.,1.,0.],[146./256,181./256,88./256],]
b = [[0.,0.,1.],[43./256,114./256,177./256],[79./256,132./256,196./256],[76./256,106./256,146./256]]
orgColors = [[r[1],g[1],b[1]]]
# orgColors = [[[228./256,36./256,35./256],[225./256,230./256,0./256],[43./256,114./256,177./256]]]
colors = []
edg = N*rad+0.1


for layers in range(N):
    drawRing(3*2**layers,layers,patches)
    orgColors += [[]]
    for index in range(3*2**layers):
        colorsApp(index, layers, orgColors)
        
# print "HHHHHHHHHHHHHHHHHH"
for i in range(len(orgColors)-1):
    colors += orgColors[i]

p = PatchCollection(patches, alpha=1.)
# p.set_array(np.array(colors))
p.set_facecolor(np.array(colors))
p.set_edgecolor('#f2f2f2')
p.set_alpha(0.9)
ax.add_collection(p) # add this patchcollection to the axe
# fig.colorbar(p, ax=ax)

plt.axis('scaled')
plt.axis('off')
plt.axis([-edg, edg, -edg, edg])
plt.show()
# plt.savefig('./colorWheel1.png', transparent = True, dpi = 100)