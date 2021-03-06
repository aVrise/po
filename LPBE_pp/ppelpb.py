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
    # if (x - a[6]).min < 0:
    #     print "exceed up_limit"
    return a[0]*x**2 + a[1]*x + a[2] #without plateau
    # return (a[3]*x+a[4])*(x>=a[5]) + (a[0]*x**2 + a[1]*x + a[2])*(x<a[5]) # with plateau

colorList = ['#070707','#B5D99C', '#F9564F', '#F3C677', '#4D7298', '#B8B3E9', '#8DDBE0', '#bebebe', '#D15700', '#EA638C' ,'#00A8E0', 'k', 'k', 'k', 'k', 'k', 'k'] #Black, Green, Red, Yellow, Blue, Purple, cyan, grey, brown, pink, deep sky blue

a = open('pp_dat_without_eff','r').readlines() # .2 for fix z0 of 0.498749; .3 for fix z0 of [0.530779,0.531069]: #psur,dsur
a1a = [x.strip().split()[0] for x in a[::2]] #code
a2 = [[float(x) for x in y.strip().split()] for y in a[1::2] if y.strip().split() != '']
x2 = np.arange(-1.0,-0.25,0.001)
# print a2

# ++ for -, + for +
c_collect=['_','2c1','2c1-1c2','1c2','1c2-c3','c3','1c3-c4++1c3+c3','c4++1c3+c3','_'] # total energy
# c_collect=['2c1++2c1','2c1-1c2++2c1','1c2++2c1','1c2-c3++1c2','c3++1c2','1c3-c4++1c3','c4++1c3'] # difference
# ca_collect=['co+dsur5l_h','1ca0','ca1','1ca1-ca4++1ca1+ca1','ca4++1ca1+ca1','1ca4-ca6++1ca1+ca1++1ca4+ca4','ca6++1ca1+ca1++1ca4+ca4'] # miss one
ca_collect=['_','1ca0','1ca0-ca1','ca1','1ca1-ca4++1ca1+ca1','ca4++1ca1+ca1','1ca4-ca6++1ca1+ca1++1ca4+ca4','ca6++1ca1+ca1++1ca4+ca4','_'] # miss one
# ca_collect=['1ca0++1ca0','ca1++1ca0','1ca1-ca4++1ca1','ca4++1ca1','1ca4-ca6++1ca4','ca6++1ca4'] # difference
# cb_collect=['co+dsur5l_h','1ca0','cb1','1cb1-cb3++1cb1+cb1','cb3++1cb1+cb1','ch2o+dsur5l++1cb1+cb1','1cb3-cb5++1cb3+cb3++1cb1+cb1','cb5++1cb3+cb3++1cb1+cb1'] # miss one
cb_collect=['_','1ca0','1ca0-ca1','cb1','1cb1-cb3++1cb1+cb1','cb3++1cb1+cb1', '1cb3-ca6++1cb3+cb3++1cb1+cb1','ca6++1cb3+cb3++1cb1+cb1','_','1ca0','1ca0-ca1','cb1','1cb1-cb3++1cb1+cb1','cb3++1cb1+cb1','1cb3-cb5++1cb3+cb3++1cb1+cb1','1cb5++1cb3+cb3++1cb1+cb1++1cb6+ca6','_'] # miss one
# cb_collect=['1ca0++1ca0','cb1++1ca0','1cb1-cb3++1cb1','cb3++1cb1','1cb3-cb5++1cb3','1cb5++1cb3++1cb1+cb1'] # difference
ce_collect=['_','1cb6','1cb6-cb7','cb7','_','1cb5','1cb5-cb7','cb7','_','1cb5','1cb5-cbv','cbv','_']
# ce_collect=['1cb6++1cb6','1cb5++1cb5','1cb5-cb7++1cb5','1cb5-cbv++1cb5','1cb6-cb7++1cb6','cbv','cb7']
# ce_collect=['1cb6','1cb5','1cb5-cb7','1cb5-cbv','1cb6-cb7','cbv','cb7','psur5l+ch4']
# co_collect=['co2+dsur5l','co2h','co2v','co_1','co2h-co2v','co2v-co_2','co+psur5l'] # adsorption
# co_collect=['_','co2h++co2h','co2h-co2v++co2h','co2v++co2h','co2v-co_2++co2v','co_1++co2v', '_'] # miss one
# co_collect=['_','co2h','co2h-co2v','co2v','co2v-co_2','co_1', '_'] # miss one
co_collect=['_','co_1','co2v-co_2','co2v','_'] # miss one
# co_collect=['co2h','co2v','co_1','co2h-co2v','co2v-co_2'] # miss one
cd_collect=['_','ca4','deots','deocloh','_']
cp_collect=['dummy+cb3++ch2o++dsur5l','dummy++ch4++dsur5l+c4','dummy++ch4+cbv++psur5l','dummy++ch3oh+cb7++dsur5l','dummy++co+co_1++psur5l','dummy++co2+co2h++dsur5l','dummy++co++dsur5l_h+1ca0']
cp1_collect=['dummy','dummy++ch2o+ch2op++psur5l','dummy+cb3++ch2o++dsur5l','dummy++ch3oh+ch3ohp++psur5l','dummy++ch3oh+cb7++dsur5l','dummy++ch4+cbv++psur5l','dummy++ch4++dsur5l+c4']
cp2_collect=['dummy','dummy++co+co_1++psur5l','dummy+ca0++dsur5l++co','dummy++co2+co2p++psur5l','dummy++co2+co2h++dsur5l','dummy++co2+co2v++dsur5l']
cdu_collect=['_','dummy','dummy1+dummy1','dummy2++dummy1','_']
cna_collect=['_','1cb3','1cb3-cb5','cb5','1cb5-cb7++1cb5+cb5','cb7++1cb5+cb5','_','1cb3','1cb3-ca6','ca6','1cb6-cb7++1cb6+ca6','cb7++1cb5+cb5','_','1cb3','1cb3-cb5','cb5','1cb5-cbv++1cb5+cb5','cbv++1cb5+cb5','_']
cnb_collect=['_','cb3','1cb1-cb3','1cb1','1ca0+1cb1++cb1','_','cb3','1cb1-cb3','1cb1','1ca1-ca4','ca4','deocloh','2c1-1c2++2c1+deocloh','1c2++2c1+deocloh','1c2-c3++2c1+deocloh','c3++2c1+deocloh','1c3-c4++1c3+c3++2c1+deocloh','c4++1c3+c3++2c1+deocloh','_']
cnb1_collect=['_','cb3','1cb1-cb3','1cb1','1ca0+1cb1++cb1','_','cb3','1cb1-cb3','1cb1','1ca1-ca4','ca4','_']
cnb2_collect=['2c1','2c1-1c2','1c2','1c2-c3','c3','1c3-c4++1c3+c3','c4++1c3+c3']
deo_collect=['_','ca6', 'deo-ts','deo-f','1c2-c3++1c2+deo-f','c3++1c2+deo-f','1c3-c4++1c3+c3++1c2+deo-f','c4++1c3+c3++1c2+deo-f','_']


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
    "cbv":[r"$(P)CH_4*$",4],
    "co2h":[r"$CO_2(H)*$",0],
    "co2h-co2v":[r"$CO_2(H)* \to CO_2(V)$*",0],
    "co2v":[r"$CO_2(V)*$",0],
    "co2v-co_2":[r"$CO_2(V)* \to CO$",0],
    "co_1":[r"$(P)CO*$",0],
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
    "co2p":["$(P)CO_2$",0],
    "ch2op":["$(P)CH_2O$",0],
    "ch3ohp":["$(P)CH_3OH$",0],
    "ca0":["$CO*$",0],
    "1cb3-ca6":[r"$CH_2O* \to CH_2OH*$",0],
    "deo-f":[r"$CH_2*+OH\cdot$",0],
    "psur5l_plot":[r"$CH_2*+OH\cdot$",0],
    "psur5l_plot_lc":[r"$CH_2*+OH\cdot$",0],
    "deo-ts":[r"$CH_2OH* \to CH_2*+OH\cdot$",0]
}

collect=['psur5l_plot++psur5l_plot_lc']
collection=deo_collect

for ii in [-0.3,-0.45,-0.6]:
    print "__",ii      
    for j,i in enumerate(collection):
        sign=1
        total=0
        if '-' in i:
            state='t'
        elif "_" == i:
            print i
            continue
        else:
            state='i'
        i=i.split('+')
        # print i
        for iii in i:
            # print ii
            if iii == '' :
                sign = 0
                continue
            elif sign == 0 : 
                k=a1a.index(iii)
                total = total - 0.5*fitFunction(ii,a2[k])
                sign=1
            elif sign == 1 :
                k=a1a.index(iii)
                total = total + 0.5*fitFunction(ii,a2[k])
        print state, total,' '.join(i)

print "__"

