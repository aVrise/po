import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats

a = open('data','r').readlines()
a = [[float(x) for x in y.strip().split()] for y in a]
x = [1./3,1./4,1./7,1./9,1./16] 
sets=[]
for i1 in a[0]:
    for i2 in a[1]:
        for i3 in a[2]:
            for i4 in a[3]:
                for i5 in a[5]:
                    j=[i1,i2,i3,i4,i5]
                    slope, intercept, r_value, p_value, std_err = stats.linregress(x,j)
                    sets.append([j,r_value**2])

sets.sort(key=lambda x:x[-1],reverse=True)
print(sets[:3])