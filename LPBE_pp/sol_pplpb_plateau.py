#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
from scipy.integrate import quad
import sys

# the function needed to be fit
def fitFunction(x, a, b, c):
    return a*x**2 + b*x + c

# fit and xdata, ydata 
def fit(x, y, fittype):
    global dat, ref_date
    deltax=0.1*(x.max()-x.min())
    x1=np.arange(x.min()-deltax, x.max()+deltax, 0.01)
    if fittype==2:
        popt, pcov = curve_fit(fitFunction, x, y)
        slope, intercept, r_value, p_value, std_err = stats.linregress((x+popt[1]/2/popt[0])**2,y)
        # xs=(2*popt[0]*ref_date[0]+np.sqrt((2*popt[0]*ref_date[0])**2-4*popt[0]*(ref_date[1]-popt[2]-popt[1]*ref_date[0])))/2/popt[0]
        print (popt[1])**2-4*popt[0]*(popt[2]-ref_date[1])
        xs=(-popt[1]+np.sqrt((popt[1])**2-4*popt[0]*(popt[2]-ref_date[1])))/2/popt[0] # No roots!
        # ys=fitFunction(xs,*popt)
        # m=(ys-ref_date[1])/(xs-ref_date[0])
        # n=ys-m*xs
        plt.plot([xs,ref_date[0]],[fitFunction(xs,*popt),ref_date[1]],'-')
        # print popt[0],"\t",popt[1],"\t",popt[2],"\t",dat[2][0]
        # print popt[0],',',popt[1],', ',popt[2],', ',dat[2,0].min(),', ',r_value**2
        # print popt[0],popt[1],popt[2],dat[2,:].min(),dat[2,:].max(),r_value**2,min((-popt[1]-np.sqrt(popt[1]**2-4*popt[0]*(popt[2]-ref_date[1])))/2/popt[0],(-popt[1]+np.sqrt(popt[1]**2-4*popt[0]*(popt[2]-ref_date[1])))/2/popt[0]),ref_date[:] # a,b,c,limit_down,limit_up,R2,root_min,ref_intel
        print popt[0],popt[1],popt[2],xs,ref_date[0] # a,b,c,xs,up_limit
        return x1, fitFunction(x1,*popt)
    elif fittype==1:
        slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
        print r_value**2, slope, intercept
        return x1, slope*x1+intercept

for aii in sys.argv[1:]:
    # format input file: "absolute q" "Total Energy" "Fermi Level" "Vacuum Level" "reference q"
    print aii
    inputFile=open(aii,'r').readlines()
    inputFile=[[float(x) for x in y.strip().split() if x != ''] for y in inputFile if y[0] != '#']
    for j,i in enumerate(inputFile):
        if abs(i[4] - i[0]) < 0.001:
            ref = i
            ref_index = j
            Eref = i[1]
            # z0=i[-1]
            break
        if abs(i[3] - i[0]) < 0.001:
            ref = i
            ref_index = j
            Eref = i[1]
            # z0=i[-1]
            break
    # z0=sys.argv[2]
  
    ref_date = [-ref[3]-ref[2]-4.44, ref[1]]
        # set vars
    # inputFile=np.array(inputFile[:])
    inputFile=np.array(inputFile[ref_index+1:])
    for zc1 in [1]: #psur,dsur
    # for zc1 in [1.36]: # debug mode
    
        ## for sol
        dat = np.array([inputFile[:, 0]-inputFile[:, 4]]) # delta_q for index[0]
        dat = np.append(dat, np.array([-inputFile[:,3]-inputFile[:,2]]), axis=0) # W for index[1] (absolute U)
        dat = np.append(dat, np.array([dat[1]-4.44]), axis=0) # U vs SHE for index[2]
        # z0 = inputFile[:,-1] - zc1*2/36.6572
        z0 = zc1 #0.498749
        dat = np.append(dat, np.array([z0*(inputFile[:,1]+inputFile[:,3]*dat[0].T-Eref)+dat[1]*dat[0].T+Eref]), axis=0) # G for index[3]
        dat = np.append(dat, np.array([dat[3]+z0*inputFile[:,5]*dat[0].T]), axis=0) # G_corr for index[4]
        dat = np.append(dat, np.array([inputFile[:,1]+inputFile[:,3]*dat[0].T+dat[1]*dat[0].T]), axis=0) # G_nonsurf for index[5]


        #plot Va vs delta-q
        # plt.figure()
        # yVa=inputFile[:,5]
        # xdeltaq=dat[0]
        # xdeltaqs, yVas= fit(xdeltaq, yVa, 1)
        # plt.plot(xdeltaq,yVa,'bo')
        # plt.plot(xdeltaqs,yVas,'k')
        # plt.xlabel("delta-q")
        # plt.ylabel("Va/V")

        # plt.savefig('./delta-qvsVa.png', transparent = True, dpi = 300)

        #plot q vs W
        # plt.figure()
        # xW=dat[1]
        # xU=dat[2]
        # ydeltaq=dat[0]
        # xUs, yqs= fit(xU, ydeltaq, 1)
        # plt.plot(xU,ydeltaq,'bo')
        # plt.plot(xUs,yqs,'k')
        # plt.xlabel("Potential vs SHE/V")
        # plt.ylabel("delta-q")

        # plt.savefig('./delta-qvsU.png', transparent = True, dpi = 300)

        # plot G vs W
        plt.figure()
        for i in [3]:
            xW=dat[1]
            xU=dat[2]
            # xW=dat[2]
            yG=dat[i]
            # print xU,yG
            xWs, yGs = fit(xU, yG, 2)
            plt.plot(xU, yG,'bo')
            plt.plot(xWs,yGs,'k')
            plt.xlabel("Potential vs SHE/V")
            plt.ylabel("G/eV")
            name=str(i)+"GvsU.png"
        # plt.savefig(name, transparent = True, dpi = 300)
plt.show()


