#!/usr/bin/env python

'''
It's temporary to plot all different e-potential from pot.csv files.
'''

import matplotlib.pyplot as plt 
import numpy as np
import sys

inputfile = sys.argv[1]
a = open(inputfile,'r').readlines()
a = [[float(x) for x in y.strip().split(',')] for y in a]
a = np.array(a)
colorList = ['#070707', '#89BD9E', '#F9564F', '#F3C677', '#4D7298', '#B8B3E9', '#8DDBE0'] #Black, Green, Red, Yellow, Blue, Purple, cyan


for i in range(len(a[0])-1):
    plt.plot(a[:,0],a[:,i+1],color = colorList[i])


plt.legend([3,4,5,6,7,8])
print inputfile
plt.show()
# print a[:10,0]