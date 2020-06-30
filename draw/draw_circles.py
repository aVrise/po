from matplotlib.patches import Ellipse, Circle, Polygon
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
def coor(m,n):
    global a
    return (float(m) - float(n)/2) * a, np.sqrt(3) / 2 * a * (float(n)) 

# ell1 = Ellipse(xy = (0.0, 0.0), width = 4, height = 8, angle = 30.0, facecolor= 'yellow', alpha=0.3)
# cir1 = Circle(xy = (0.0, 0.0), radius=2, alpha=0.5)
# ax.add_patch(cir1)
colorList = ['#070707','#B5D99C', '#F9564F', '#F3C677', '#4D7298', '#B8B3E9', '#8DDBE0', '#bebebe', '#D15700', '#EA638C' ,'#00A8E0', 'k', 'k', 'k', 'k', 'k', 'k'] #Black, Green, Red, Yellow, Blue, Purple, cyan, grey, brown, pink, deep sky blue

a = 5.5
# two default circles
ax.add_patch(Circle(xy = (coor(2,2)), radius=1.5, color=colorList[1]))
ax.add_patch(Circle(xy = (1.5*a, 1.5*np.sqrt(3)*a), radius=1.5, color=colorList[2]))
# substrate
for i in range(7):
# for i in range(8):
    x = - i * a / 2
    y = i * a * np.sqrt(3) / 2
    for j in range(8):
        ax.add_patch(Circle(xy = (x, y), radius=1.5, fill=False, ec=colorList[0],lw=1.5))
        x = x + a
# unit cell
# cells=[[[1,1],[1,5],[5,5],[5,1]],[[1,1],[1,4],[4,4],[4,1]],[[1,1],[1,3],[3,3],[3,1]],[[1,1],[1,2],[2,2],[2,1]],[[1,1],[5,3],[7,7],[3,5]],[[1,1],[4,2],[6,5],[3,4]],[[1,1],[3,2],[4,4],[2,3]]]
cells=[[[1,1],[1,5],[5,5],[5,1]],[[1,1],[1,4],[4,4],[4,1]],[[1,1],[1,3],[3,3],[3,1]],[[1,1],[1,2],[2,2],[2,1]],[[1,1],[4,2],[6,5],[3,4]],[[1,1],[3,2],[4,4],[2,3]]]
cells=[np.array([coor(x[0],x[1]) for x in y]) for y in cells]
# print(cells)
for i in range(len(cells)):
    ax.add_patch(Polygon(xy = cells[i], fill=False, ec=colorList[3+i], lw=3))
# legend of unit cells
# legend1=[[[-3.5*a,0*a*np.sqrt(3)/2],[-2.5*a,0*a*np.sqrt(3)/2]],[[-3.5*a,1*a*np.sqrt(3)/2],[-2.5*a,1*a*np.sqrt(3)/2]],[[-3.5*a,2*a*np.sqrt(3)/2],[-2.5*a,2*a*np.sqrt(3)/2]],[[-3.5*a,3*a*np.sqrt(3)/2],[-2.5*a,3*a*np.sqrt(3)/2]],[[-3.5*a,0.5*a*np.sqrt(3)/2],[-2.5*a,0.5*a*np.sqrt(3)/2]],[[-3.5*a,1.5*a*np.sqrt(3)/2],[-2.5*a,1.5*a*np.sqrt(3)/2]],[[-3.5*a,2.5*a*np.sqrt(3)/2],[-2.5*a,2.5*a*np.sqrt(3)/2]]]
legend1=[[[-3.5,0],[-3,0]],[[-3.25,0.5],[-2.75,0.5]],[[-2.75,1.5],[-2.25,1.5]],[[-2.25,2.5],[-1.75,2.5]],[[-3.,1],[-2.5,1]],[[-2.5,2],[-2.,2]]]
# legend1t=[r'$(4 \times 4)$',r'$(3 \times 3)$',r'$(2 \times 2)$',r'$(1 \times 1)$',r'$(2\sqrt{3} \times 2\sqrt{3})$',r'$(\sqrt{10} \times \sqrt{10})$',r'$(\sqrt{3} \times \sqrt{3})$']
legend1t=[r'$(4 \times 4)$',r'$(3 \times 3)$',r'$(2 \times 2)$',r'$(1 \times 1)$',r'$(\sqrt{10} \times \sqrt{13})$',r'$(\sqrt{3} \times \sqrt{3})$']
legend1=[np.array([coor(x[0],x[1]) for x in y]) for y in legend1]
# print(legend1)
for i in range(len(legend1)):
    ax.plot(legend1[i][:,0]-1.5,legend1[i][:,1],'-',lw=1.5,color=colorList[3+i])
    ax.text(legend1[i][1,0]-.5, legend1[i][0,1],legend1t[i],verticalalignment='center', fontsize=8)

# legend of circles
# ax.add_patch(Circle(xy = coor(10.5, 7), radius=1.5, fill=False, ec=colorList[0],lw=1.5))
# ax.add_patch(Circle(xy = coor(10, 6), radius=1.5, color=colorList[1], ec=colorList[0],lw=1.5))
# ax.add_patch(Circle(xy = coor(9.5, 5), radius=1.5, color=colorList[2], ec=colorList[0],lw=1.5))
ax.add_patch(Circle(xy = coor(10, 6), radius=1.5, fill=False, ec=colorList[0],lw=1.5))
ax.add_patch(Circle(xy = coor(9.5, 5), radius=1.5, color=colorList[1], ec=None))
ax.add_patch(Circle(xy = coor(9, 4), radius=1.5, color=colorList[2], ec=None))
# ax.text(coor(10.5, 7)[0]-4,coor(10.5, 7)[1],r"$O_s$",horizontalalignment='center',verticalalignment='center', fontsize=12)
# ax.text(coor(10, 6)[0]-4,coor(10, 6)[1],r"$H$",horizontalalignment='right', verticalalignment='center', fontsize=12)
# ax.text(coor(9.5, 5)[0]-4,coor(9.5, 5)[1],r"$CO$",horizontalalignment='right', verticalalignment='center', fontsize=12)
ax.text(coor(10, 6)[0]-4,coor(10, 6)[1],r"$O_s$",horizontalalignment='center',verticalalignment='center', fontsize=12)
ax.text(coor(9.5, 5)[0]-4,coor(9.5, 5)[1],r"$H$",horizontalalignment='right', verticalalignment='center', fontsize=12)
ax.text(coor(9, 4)[0]-4,coor(9, 4)[1],r"$CO$",horizontalalignment='right', verticalalignment='center', fontsize=12)
 
plt.axis('scaled')
# ax.set_xlim(-4, 4)
# ax.set_ylim(-4, 4)
plt.axis('equal')   #changes limits of x or y axis so that equal increments of x and y have the same length
# plt.xticks([])
# plt.yticks([])
plt.axis('off')
# plt.show()
plt.savefig('../out/scheme2_toc.png', transparent = False, dpi = 1000,pad_inches=0,bbox_inches='tight')