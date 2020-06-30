#!/usr/bin/env python

'''
to put all lines of potential_plot together
input file format:
./cb7/sol/ce-cb7-sol_debye-dddd  name # pathway or name
-2.333437075325563      18.608447030181836      -1469.0598992426226     1.9918181499999994 # a b c d ## a*x**2 + b*x +c, d is the maximum of x 
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
from scipy.integrate import quad
import sys

# the function needed to be fit
def fitFunction(x, a):
    # print x,a
    return a[0]*x**2 + a[1]*x + a[2]

def correct_coefficient(i):
    # 0 for a, else for sol
    # co_dsur_a=[-0.8609439907770506 , -1.7019608056678648 , -1375.2024582527629 , -1.3219000000000003 , 0.9845485096917134] modified@0514
    # co_dsur_sol=[-0.7961741041845686 , 3.204449538244873 ,  -1381.3705952073512 ,  2.5334052599999994 ,  0.9999303779825229] modified@0514
    # co_dsur_h_a=[-0.4562665308877652,-0.8495854759501174,-1382.5092168676438,-2.1408500000000004,0.9998758994277227] modified@0514
    # co_dsur_h_sol=[-1.1106870035776935 , 4.614684044155109 ,  -1390.3394014149037 ,  1.8754658499999994 ,  0.9999976296931078] modified@0514
    # co_psur_a=[-0.675542751642963 , -0.9956021382343142 , -1391.6067045768218 , -0.8038300000000005 , 0.9995040379973243] modified@0514
    # co_psur_sol=[-0.8044125213214458 , 3.842852659640776 ,  -1399.2420084635987 ,  3.0027610399999993 ,  0.9997490252964718] modified@0514    
    if i == 0:
        return np.array([-0.4562665308877652,-0.8495854759501174,-1382.5092168676438]) - np.array([-0.8609439907770506 , -1.7019608056678648 , -1375.2024582527629])
    else:
        return np.array([-1.0642810952202095,4.9561944347501266,-1447.4097779638441]) - np.array([-0.9259333410874787,4.73907350041153,-1440.7159892758307 ])
       
        # return np.array([-1.1106870035776935 , 4.614684044155109 ,  -1390.3394014149037]) - np.array([-0.7961741041845686 , 3.204449538244873 ,  -1381.3705952073512 ])

# fit and xdata, ydata 
def fit(x, y, fittype):
    deltax=0.1*(x.max()-x.min())
    x1=np.arange(x.min()-deltax, x.max()+deltax, 0.01)
    if fittype==2:
        popt, pcov = curve_fit(fitFunction, x, y)
        print popt[0],"\t",popt[1],"\t",popt[2],"\t"
        return x1, fitFunction(x1,*popt)
    elif fittype==1:
        slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
        print r_value**2
        return x1, slope*x1+intercept

colorList = ['#070707', '#89BD9E', '#F9564F', '#F3C677', '#4D7298', '#B8B3E9', '#8DDBE0', 'r', 'k', 'k'] #Black, Green, Red, Yellow, Blue, Purple, cyan
sol=[]
vac=[]


a = open('pp_dat_a','r').readlines()
a1a = [x.strip().split()[0] for x in a[::3]] #code
a1b = [x.strip().split()[1] for x in a[::3]] #name
# a1c = [int(x.strip().split()[2]) for x in a[::2]] #sol or not, 0 for vac, 1 for sol
a1d = [int(x.strip().split()[2]) for x in a[::3]] #number of hydrogen atoms
a2 = np.array([[float(x) for x in y.strip().split()] for y in a[1::3] if y.strip().split() != '']) # 2 for vac
a3 = np.array([[float(x) for x in y.strip().split()] for y in a[2::3] if y.strip().split() != '']) # 3 for sol
x2 = np.arange(-2.2,min(-0.5164698200000006,a2[:,3].min()),0.01)
x3 = np.arange(-2.2,min(1.8754658499999994,a3[:,3].min()),0.01)
# print a2,a3

c_collect=['2c1','2c1-1c2','1c2','1c2-c3','1c3','1c3-c4','c4']
ca_collect=['1ca0','1ca0-ca1','1ca1','1ca1-ca4','1ca4','1ca4-ca6','ca6']
cb_collect=['1ca0','1ca0-ca1','1cb1','1cb1-cb3','1cb3','1cb3-cb5','cb5']
ce_collect=['1cb6','1cb5','1cb5-cb7','1cb5-cbv','1cb6-cb7','cbv','cb7']
co2_collect=['co2h','co2v','co_1','co_1-co2h','co2h-co2v','co2v-co_2']

#plot all
# for i in range(len(a1)):
#     plt.plot(x,fitFunction(x,a2[i]),color = colorList[i])

#plot selected code 
# collection=['1cb6','ca6']
collection=c_collect
for j,i in enumerate(collection):
    k=a1a.index(i)
    # plt.plot(x2,0.5*fitFunction(x2,a2[k,:3]-a1d[k]*correct_coefficient(0)),'--',color = colorList[j])
    plt.plot(x3,fitFunction(x3,a3[k,:3]-a1d[k]*correct_coefficient(1))/2,color = colorList[j],label=i)
    # plt.plot(x3,fitFunction(x3,a3[k,:3])/2,color = colorList[j],label=i)

plt.ylabel('Energy/eV')
plt.xlabel('Potential vs SHE/V')
plt.legend(frameon=False,loc=4)

plt.show()
# print a2[:,3].min()
# for i in range(len(a1a)):
#     print a1a[i],a1b[i],a1d[i]
#     print a2[i]
#     print a3[i]