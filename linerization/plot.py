import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

a = open('data','r').readlines()
a = [float(y.strip()) for y in a]
# x = [1./3,1./4,1./7,1./9,1./12,1./16]
x = [1./3,1./4,1./7,1./9,1./16]
# x = [1., 1./3,1./4,1./7,1./9,1./12,1./16]
# x = [1./3,1./4,1./7,1./9,1./16]
# x = [-0.27,-0.30,-0.30,-0.30,-0.36,-0.31]
# x = [-0.359, -0.295, -0.394, -0.239, -0.331]

# print x,a[0:-2]

slope, intercept, r_value, p_value, std_err = stats.linregress(x,a[:-1])
# slope, intercept, r_value, p_value, std_err = stats.linregress(x,a) # h
x0 = np.arange(0.,0.41,0.01)
# x0 = np.arange(-0.4,-0.2,0.01)
y0 = slope * x0 + intercept

ax = plt.subplot(111)
ax.plot(x,a[:-1],'bo')
# plt.plot(x,a,'bx')
ax.plot(x0,y0,'b')
ax.plot(x0,[a[-1]]*len(x0),'k')
# plt.plot(-0.33,a[-1],'kx')
# np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
# locs, labels = plt.yticks()
# locs.set_printoptions(formatter={'float': '{: 0.3f}'.format})MultipleLocator(0.01)
ax.yaxis.set_major_locator(MultipleLocator(0.15))
plt.xlabel(r'$\theta$ / ML',fontsize=14,labelpad=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.ylabel('Energy / eV',labelpad=5, fontsize=14)

# print a[-1]-intercept,(a[-1]-intercept)/a[-1], r_value**2
print "y =",slope,"x +",intercept,r_value**2, a[-1]-intercept, slope/(a[-1]-intercept)

# plt.show()
plt.savefig('../out/Ev.jpg', transparent = True, dpi = 150,pad_inches=0,bbox_inches='tight')
