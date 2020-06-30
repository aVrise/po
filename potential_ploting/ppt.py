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

colorList = ['#070707','#B5D99C', '#F9564F', '#F3C677', '#4D7298', '#B8B3E9', '#8DDBE0', '#bebebe', '#D15700', '#EA638C' ,'#00A8E0', 'k', 'k', 'k', 'k', 'k', 'k'] #Black, Green, Red, Yellow, Blue, Purple, cyan, grey, brown, pink, deep sky blue

a = open('pp_dat_t.3','r').readlines() # .2 for fix z0 of 0.498749; .3 for fix z0 of [0.530779,0.531069]: #psur,dsur
a1a = [x.strip().split()[0] for x in a[::3]] #code
# a1b = [x.strip().split()[1] for x in a[::3]] #name
# a1c = [int(x.strip().split()[2]) for x in a[::2]] #sol or not, 0 for vac, 1 for sol
# a1d = [int(x.strip().split()[1]) for x in a[::3]] #number of hydrogen atoms
a2 = np.array([[float(x) for x in y.strip().split()] for y in a[1::3] if y.strip().split() != '']) # 2 for vac
a3 = np.array([[float(x) for x in y.strip().split()] for y in a[2::3] if y.strip().split() != '']) # 3 for sol
# x2 = np.arange(-2.2,min(-0.5164698200000006,a2[:,3].min()),0.01)
# x2 = x3 = np.arange(-2.2,min(2.2,a3[:,3].min()),0.01)
x2 = x3 = np.arange(-1.0,-0.28,0.001)
# print a2,a3

# ++ for -, + for +
c_collect=['2c1','2c1-1c2','1c2','1c2-c3','c3','1c3-c4++1c3+c3','c4++1c3+c3'] # total energy
# c_collect=['2c1++2c1','2c1-1c2++2c1','1c2++2c1','1c2-c3++1c2','c3++1c2','1c3-c4++1c3','c4++1c3'] # difference
# ca_collect=['co+dsur5l_h','1ca0','ca1','1ca1-ca4++1ca1+ca1','ca4++1ca1+ca1','1ca4-ca6++1ca1+ca1++1ca4+ca4','ca6++1ca1+ca1++1ca4+ca4'] # miss one
ca_collect=['1ca0','ca1','1ca1-ca4++1ca1+ca1','ca4++1ca1+ca1','1ca4-ca6++1ca1+ca1++1ca4+ca4','ca6++1ca1+ca1++1ca4+ca4'] # miss one
# ca_collect=['1ca0++1ca0','ca1++1ca0','1ca1-ca4++1ca1','ca4++1ca1','1ca4-ca6++1ca4','ca6++1ca4'] # difference
# cb_collect=['co+dsur5l_h','1ca0','cb1','1cb1-cb3++1cb1+cb1','cb3++1cb1+cb1','ch2o+dsur5l++1cb1+cb1','1cb3-cb5++1cb3+cb3++1cb1+cb1','cb5++1cb3+cb3++1cb1+cb1'] # miss one
cb_collect=['1ca0','cb1','1cb1-cb3++1cb1+cb1','cb3++1cb1+cb1','1cb3-cb5++1cb3+cb3++1cb1+cb1','cb5++1cb3+cb3++1cb1+cb1'] # miss one
# cb_collect=['1ca0++1ca0','cb1++1ca0','1cb1-cb3++1cb1','cb3++1cb1','1cb3-cb5++1cb3','1cb5++1cb3++1cb6+ca6'] # difference
ce_collect=['1cb6','1cb5','1cb5-cb7','1cb5-cbv','1cb6-cb7','cbv','cb7']
# ce_collect=['1cb6++1cb6','1cb5++1cb5','1cb5-cb7++1cb5','1cb5-cbv++1cb5','1cb6-cb7++1cb6','cbv','cb7']
# ce_collect=['1cb6','1cb5','1cb5-cb7','1cb5-cbv','1cb6-cb7','cbv','cb7','psur5l+ch4']
# co_collect=['co2h','co2h-co2v','co2v','co2v-co_2','co_1'] # adsorption
co_collect=['co2v','co2v-co_2','co_1'] # adsorption
# co_collect=['co2h++co2h','co2v++co2h','co_1++co2v','co2h-co2v++co2h','co2v-co_2++co2v'] # difference
# co_collect=['co2h','co2v','co_1','co2h-co2v','co2v-co_2'] # miss one
cd_collect=['ca4','deocloh']
cp1_collect=['dummy','dummy++ch2o+ch2op++psur5l','dummy+cb3++ch2o++dsur5l','dummy++ch3oh+ch3ohp++psur5l','dummy++ch3oh+cb7++dsur5l','dummy++ch4+cbv++psur5l','dummy++ch4++dsur5l+c4']
cp2_collect=['dummy','dummy++co+co_1++psur5l','dummy+ca0++dsur5l++co','dummy++co2+co2p++psur5l','dummy++co2+co2h++dsur5l','dummy++co2+co2v++dsur5l']
cdu_collect=['dummy','dummy1+dummy1','dummy2++dummy1']
ct_collect=['1cb3','ca6']
cna_collect=['1cb3', '1cb3-ca6','ca6','1cb6-cb7++1cb6+ca6','cb7++1cb5+cb5','1cb3-cb5','cb5','1cb5-cb7++1cb5+cb5','1cb5-cbv++1cb5+cb5','cbv++1cb5+cb5']
cnb_collect=['cb3','1cb1-cb3','1cb1','1ca0+1cb1++cb1','1ca1-ca4','ca4','deocloh','2c1-1c2++2c1+deocloh','1c2++2c1+deocloh','1c2-c3++2c1+deocloh','c3++2c1+deocloh','1c3-c4++1c3+c3++2c1+deocloh','c4++1c3+c3++2c1+deocloh']
# cnb1_collect=['cb3','1cb1-cb3','1cb1','1ca0+1cb1++cb1','1ca1-ca4','ca4']
# cnb2_collect=['2c1','2c1-1c2','1c2','1c2-c3','c3','1c3-c4++1c3+c3','c4++1c3+c3']
deo_collect=['ca6', 'deo-ts','deo-f','1c2-c3++1c2+deo-f','c3++1c2+deo-f','1c3-c4++1c3+c3++1c2+deo-f','c4++1c3+c3++1c2+deo-f']

name={
    "2c1":[r"$CH*$",3],
    "1c2":[r"$CH_2*$",3],
    "1c2-c3": [r"$CH_2* \to CH_3*$",3],
    "1c3":[r"$CH_3*$",4],   
    "c3":[r"$CH_3*$",4],
    "1c3-c4":[r"$CH_3* \to CH_4*$",4],
    "1ca0":[r"$CO*$",1],
    "1ca0-ca1":[r"$CO* \to CHO$",1],
    "1ca1":[r"$CHO*$",2],
    "ca1":[r"$CHO*$",2],
    "1ca1-ca4":[r"$CHO* \to CHOH*$",2],
    "1ca4":[r"$CHOH*$",3],
    "ca4":[r"$CHOH*$",3],
    "1ca4-ca6":[r"$CHOH* \to CH_2OH*$",3],
    "1cb1":[r"$CHO*$",2],
    "cb1":[r"$CHO*$",2],
    "1cb1-cb3":[r"$CHO* \to CH_2O*$",2],
    "1cb3":[r"$CH_2O*$",3],
    "cb3":[r"$CH_2O*$",3],
    "1cb3-cb5":[r"$CH_2O* \to CH_3O*$",3],
    "1cb5":[r"$CH_3O*$",4],
    "1cb5-cb7":[r"$CH_3O* \to CH_3OH*$",4],
    "1cb5-cbv":[r"$CH_3O* \to CH_4*$",4],
    "1cb6":[r"$CH_2OH*$",4],
    "1cb6-cb7":[r"$CH_2OH* \to CH_3OH*$",4],
    "2c1-1c2":[r"$CH* \to CH_2*$",3],
    "c4":[r"$CH_4*$",4],
    "ca6":[r"$CH_2OH*$",3],
    "cb5":[r"$CH_3O*$",3],
    "cb7":[r"$CH_3OH*$",4],
    "cbv":[r"$CH_4*$",4],
    "co2h":[r"$CO_2(H)*$",0],
    "co2h-co2v":[r"$CO_2(H)* \to CO_2(V)$*",0],
    "co2v":[r"$CO_2(V)*$",0],
    "co2v-co_2":[r"$CO_2(V)* \to CO$",0],
    "co_1":[r"$CO*$",0],
    "co_1-co2h":[r"$CO* \to CO_2(H)*$",0],
    "psur5l":["",0],
    "dsur5l":["dsur",0],
    "dsur5l_h":["",0],
    "ch4":["ch4",4],
    "ch3oh":["ch3oh",4],
    "co2":["co2",0],
    "co":["co",0],
    "ch2o":["ch2o",0],
    "deots":["",0],
    "deocloh":["",0],
    "dummy":["0",0],
    "dummy1":["1",0],
    "dummy2":["2",0],
    "co2p":["co2",0],
    "ch2op":["ch2o",0],
    "ch3ohp":["ch3ohp",0],
    "ca0":["ca0",0],
    "1cb3-ca6":[r"$CH_2O* \to CH_2OH*$",0],
    "deo-f":[r"$CH_2*+OH\cdot$",0],
    "deo-ts":[r"$CH_2OH* \to CH_2*+OH\cdot$",0]
}

# correct_coefficient=a2[a1a.index("dsur5l_h"),:3]-a2[a1a.index("dsur5l"),:3]
# correct_coefficient=(a2[a1a.index("1cb6"),:3]-a2[a1a.index("ca6"),:3]+a2[a1a.index("1cb5"),:3]-a2[a1a.index("cb5"),:3])/2

collect=['cbv','cb7']
collection=cp1_collect
fig = plt.figure()
fig.set_size_inches(6,8)
# print a1a

for j,i in enumerate(collection):
    sign=1
    total=np.array([0,0,0])
    i=i.split('+')
    # print i
    for ii in i:
        # print ii
        if ii == '' :
            sign = 0
            continue
        elif sign == 0 : 
            k=a1a.index(ii)
            total = total - a2[k,:3]
            sign=1
        elif sign == 1 :
            k=a1a.index(ii)
            # print total,a2
            total = total + a2[k,:3]

    # print i
    # for ii in i :
    #     ii=ii.split('+')
    #     for iii in ii :
    #         k=a1a.index(iii)

    # k=a1a.index(i)
    plt.plot(x2,0.5*fitFunction(x2,total),color = colorList[j],label=name[i[0]][0],linewidth=3)
    # plt.plot(x2,0.5*fitFunction(x2,a2[k,:3]),color = colorList[j],label=name[i][0])
    # plt.plot(x3,fitFunction(x3,a3[k,:3]-name[i][1]*correct_coefficient)/2,color = colorList[j],label=name[i][0])
    # plt.plot(x3,fitFunction(x3,a3[k,:3])/2,color = colorList[j],label=i)
    # for i in x2:
    #     if fitFunction(i,total)*fitFunction(i+0.001,total) < 0:
    #         print i
# xmin, xmax = plt.xlim()
# ymin, ymax = plt.ylim()
# plt.axis([xmin, xmax, ymin-0.1*ymax,ymax])
# plt.xticks([-1.0,-0.8,-0.6,-0.4,-0.2],fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel(r'$Halved \  E^{free} \  / \ eV$',labelpad=18,fontsize=16)
plt.ylabel(r'$E_{ads} \  / \ eV$',labelpad=5,fontsize=18)
plt.xlabel(r'$\phi_{SHE}\  /\  V$',labelpad=14,fontsize=16)
# plt.ylim(ymin=-0.8) 
plt.legend(frameon=False,fontsize=12)


plt.show()
# print a2[:,3].min()
# for i in range(len(a1a)):
#     print a1a[i],a1b[i],a1d[i]
#     print a2[i]
#     print a3[i]


# plt.savefig('cp1_thesis.tiff', transparent = True, dpi = 300,pad_inches=0,bbox_inches='tight')
