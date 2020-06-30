#!/usr/bin/env python

'''
to put all lines of potential_plot together
input file format:
./cb7/sol/ce-cb7-sol_debye-dddd  name # pathway or name
-2.333437075325563      18.608447030181836      -1469.0598992426226     1.9918181499999994 # a b c m n xs up_limit ## a*x**2 + b*x +c, d is the maximum of x 
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
from scipy.integrate import quad
import sys

# the function needed to be fit
def fitFunction(x, a):
    # # a 0, b 1, c 2, m 3, n 4, xs 5, up_limit 6
    if (x - a[6]).min < 0:
        print "exceed up_limit"
    return a[0]*x**2 + a[1]*x + a[2] #without plateau
    # return (a[3]*x+a[4])*(x>=a[5]) + (a[0]*x**2 + a[1]*x + a[2])*(x<a[5]) # with plateau

colorList = ['#070707','#B5D99C', '#F9564F', '#F3C677', '#4D7298', '#B8B3E9', '#8DDBE0', '#bebebe', '#D15700', '#EA638C' ,'#00A8E0', 'k', 'k', 'k', 'k', 'k', 'k'] #Black, Green, Red, Yellow, Blue, Purple, cyan, grey, brown, pink, deep sky blue

a = open('pp_dat_without_eff','r').readlines() # .2 for fix z0 of 0.498749; .3 for fix z0 of [0.530779,0.531069]: #psur,dsur
a1a = [x.strip().split()[0] for x in a[::2]] #code
a2 = [[float(x) for x in y.strip().split()] for y in a[1::2] if y.strip().split() != '']
x2 = np.arange(-0.6,-0.28,0.001)
# print a2
# ++ for -, + for +
c_collect=['2c1','2c1-1c2','1c2','1c2-c3','c3','1c3-c4++1c3+c3','c4++1c3+c3'] # total energy
ca_collect=['1ca0', '1ca0-ca1','ca1','1ca1-ca4++1ca1+ca1','ca4++1ca1+ca1','1ca4-ca6++1ca1+ca1++1ca4+ca4','ca6++1ca1+ca1++1ca4+ca4'] # miss one
cb_collect=['1ca0','1ca0-ca1','cb1','1cb1-cb3++1cb1+cb1','cb3++1cb1+cb1','1cb3-cb5++1cb3+cb3++1cb1+cb1','cb5++1cb3+cb3++1cb1+cb1', '1cb3-ca6++1cb3+cb3++1cb1+cb1','ca6++1cb3+cb3++1cb1+cb1'] # miss one
ce_collect=['1cb6','1cb5','1cb5-cb7','1cb5-cbv','1cb6-cb7','cbv','cb7']
co_collect=['co2v','co2v-co_2','co_1'] # adsorption
cd_collect=['ca4','deocloh']
cp1_collect=['dummy','ch2op++ch2o++psur5l','cb3++ch2o++dsur5l','ch3ohp++ch3oh++psur5l','cb7++ch3oh++dsur5l','cbv++ch4++psur5l','c4++ch4++dsur5l']
cp2_collect=['dummy','co_1++co++psur5l','ca0++dsur5l++co','co2p++co2++psur5l','co2h++co2++dsur5l','co2v++co2++dsur5l']
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
    "1cb5-cbv":[r"$CH_3O* \to (P)CH_4*$",4],
    "1cb6":[r"$CH_2OH*$",4],
    "1cb6-cb7":[r"$CH_2OH* \to CH_3OH*$",4],
    "2c1-1c2":[r"$CH* \to CH_2*$",3],
    "c4":[r"$CH_4$",4],
    "ca6":[r"$CH_2OH*$",3],
    "cb5":[r"$CH_3O*$",3],
    "cb7":[r"$CH_3OH*$",4],
    "cbv":[r"$(P)CH_4$",4],
    "co2h":[r"$CO_2(H)*$",0],
    "co2h-co2v":[r"$CO_2(H)* \to CO_2(V)$*",0],
    "co2v":[r"$CO_2(V)*$",0],
    "co2v-co_2":[r"$CO_2(V)* \to (P)CO$",0],
    "co_1":[r"$(P)CO$",0],
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
    "co2p":["$(P)CO_2*$",0],
    "ch2op":["$(P)CH_2O*$",0],
    "ch3ohp":["$(P)CH_3OH*$",0],
    "ca0":["$CO*$",0],
    "1cb3-ca6":[r"$CH_2O* \to CH_2OH*$",0],
    "deo-f":[r"$CH_2*+OH\cdot$",0],
    "psur5l_plot":[r"30",0],
    "psur5l_plot_lc":[r"80",0],
    "deo-ts":[r"$CH_2OH* \to CH_2*+OH\cdot$",0],
    "plot_plc4":["40",0],
    "plot_plc5":["50",0],
    "plot_ch3oh":["ch3oh",0],
    "plot_ch3ohd":["ch3ohd",0],
    "plot_plc6":["60",0]
}

collect=['plot_ch3oh++psur5l_plot_lc++ch3ohp+psur5l']
collection=deo_collect
fig = plt.figure()
fig.set_size_inches(6,8)
# print a1a

for j,i in enumerate(collection):
    sign=1
    total=x2*0
    i=i.split('+')
    # print i
    for ii in i:
        # print ii
        if ii == '' :
            sign = 0
            continue
        elif sign == 0 : 
            k=a1a.index(ii)
            total = total - 0.5*fitFunction(x2,a2[k])
            sign=1
        elif sign == 1 :
            k=a1a.index(ii)
            # print a2[k]
            # print total, np.array(a2[k])[:5]
            total = total + 0.5*fitFunction(x2,a2[k])

    # print i
    # for ii in i :
    #     ii=ii.split('+')
    #     for iii in ii :
    #         k=a1a.index(iii)

    # k=a1a.index(i)
    plt.plot(x2,total,color = colorList[j],label=name[i[0]][0],linewidth=3)
    # plt.plot(x2,0.5*fitFunction(x2,a2[k,:3]),color = colorList[j],label=name[i][0])
    # plt.plot(x3,fitFunction(x3,a3[k,:3]-name[i][1]*correct_coefficient)/2,color = colorList[j],label=name[i][0])
    # plt.plot(x3,fitFunction(x3,a3[k,:3])/2,color = colorList[j],label=i)
    # temp = 999
    # for it,jt in enumerate(total):
    #     if temp == 999:
    #         temp = jt
    #     elif temp * jt <= 0:
    #         print name[i[0]][0], x2[it]
    #         break
# xmin, xmax = plt.xlim()
# ymin, ymax = plt.ylim()
# plt.axis([xmin, xmax, ymin-0.1*ymax,ymax])
# plt.xticks([-1.0,-0.8,-0.6,-0.4,-0.2],fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel(r'$Halved \  E^{free} \  / \ eV$',labelpad=18,fontsize=16)
# plt.ylabel(r'$E_{ads} \  / \ eV$',labelpad=5,fontsize=18)
plt.xlabel(r'$\phi_{SHE}\  /\  V$',labelpad=14,fontsize=16)
# plt.ylim(ymin=-0.8) 
# plt.ylim(ymax=-718) 
# plt.legend(frameon=False,fontsize=12,loc="lower right")


# plt.show()
plt.savefig('lpb_deo_hr.tiff', transparent = True, dpi = 1000,pad_inches=0,bbox_inches='tight')
