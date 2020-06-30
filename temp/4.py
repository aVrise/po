

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
import math

def b(x):
    return np.log2(2.)/np.log2(1.+x)


def s(t):
    return 33.05050*np.log1p(t/1000-1) + 12.22940*t/1000 -12.06510/2*(t/1000)**2 + 4.385330 /3* (t/1000)**3-0.159494/2/(t/1000)**2+259.0290

def c(t):
    return 33.05050+12.22940*(t/1000)-12.06510*((t/1000)**2) + 4.385330* ((t/1000)**3)-0.159494/((t/1000)**2)

def d(x):
    return x**4-np.pi**2*0.25*x**2

def f(x):
    return np.exp(-x**2)

def g(x, a):
    return a[0]*x**2 + a[1]*x + a[2]

f=open('data','r').readlines()
f=[[x for x in y.strip().split() if x != ''] for y in f]
f=np.array([[float(x) for x in y[1:4]]for y in f])

a1=(f[3]-f[2]-f[1]+f[0])/2
# a2=(f[1]-f[0])
# a3=f[0]
# a4=f[1]-(f[3]-f[2])
# b1=f[8]
b2=(f[9]-f[8]-(f[7]-f[6]))/2
# b3=f[6]
# b4=(f[7]-f[6]-(f[9]-f[8]))/2

a=np.arange(-3,2,0.01)
c1=np.array([-0.9265892610614264,4.770198465348647,-1437.5682031138929])
c2=np.array([-1.0280133269474196,4.914455973601439,-1444.473831549925])
d1=np.array([-0.9259333410874787,4.73907350041153,-1440.7159892758307])
d2=np.array([-1.0642810952202095,4.9561944347501266,-1447.4097779638441])
c=c2-c1-d2+d1

# for i in a:
#     d.append(quad(b, 0.01, i)[0])


# b=(a*s(a)-a[0]*s(a[0]))/96485
plt.plot(a,g(a,a1),'k')
# plt.plot(a,g(a,a2),'r')
plt.plot(a,g(a,c),'k--')
# plt.plot(a,g(a,b4),'r--')
plt.show()
