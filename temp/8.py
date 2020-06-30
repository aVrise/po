import numpy as np 
import matplotlib.pyplot as plt 

def fitFunction(x, a, b, c):
    return a*x**2 + b*x + c


def f(x):
    return 0.1*np.sin(x)

def g(x):
    return x*0
# a=[[1,2,-3],[2,1,-3],[3,1,-2],[-2,3,1],[-3,-1,3]]
# b=np.array(a[0])
# c=(b>0)*a[3]+a[1]
# print c


x1=np.arange(-20,0,0.01)
x2=np.arange(0,10,0.01)

plt.plot(x1,f(x1),'k',linewidth=3)
plt.plot(x2,g(x2),'k',linewidth=3)



# x=np.arange(-10,10,0.01)
# for popt in a:
#     x0=min((-popt[1]-np.sqrt(popt[1]**2-4*popt[0]*popt[2]))/2/popt[0],(-popt[1]+np.sqrt(popt[1]**2-4*popt[0]*popt[2]))/2/popt[0])
#     plt.plot(x0,0,'bx')
#     plt.plot(x,fitFunction(x,popt[0],popt[1],popt[2]),'k')
# plt.plot(x,x*0,'g')

plt.ylim([-1,1])
# plt.show()

plt.savefig("wave.png",transparent=True)