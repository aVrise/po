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
    global dat
    deltax=0.1*(x.max()-x.min())
    x1=np.arange(x.min()-deltax, x.max()+deltax, 0.01)
    if fittype==2:
        popt, pcov = curve_fit(fitFunction, x, y)
        # print popt[0],"\t",popt[1],"\t",popt[2]
        slope, intercept, r_value, p_value, std_err = stats.linregress((x+popt[1]/2/popt[0])**2,y)
        print popt[0],',',popt[1],',',popt[2],',',dat[2,:].min(),',',r_value**2
        return x1, fitFunction(x1,*popt)
    elif fittype==1:
        slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
        print r_value**2
        return x1, slope*x1+intercept

for aii in sys.argv[1:]:
# format input file: "absolute q" "Total Energy" "Fermi Level" "Vacuum Level" "reference q"
# a=sys.argv[1]
    print aii
    inputFile=open(aii,'r').readlines()
    inputFile=[[float(x) for x in y.strip().split() if x != ''] for y in inputFile if y[0] != '#']
    for j,i in enumerate(inputFile):
        if abs(i[-2] - i[0]) < 0.001:
            ref = i
            ref_index = j
            Eref = i[1]
            break


    # set vars
    inputFile=np.array(inputFile[ref_index+1:])
    # ref=np.array(ref)
    # print inputFile[:, 2],inputFile[:, 3]+inputFile[:, 5]
    z0=0.50279904 #average
    # z0=0.500724 #dsur_h
    # z0=0.424322 #dsur
    # z0=0.426112 #psur
    # construct dat
    dat = np.array([inputFile[:, 0]-inputFile[:, 4]]) # delta_q for index[0]
    dat = np.append(dat, np.array([inputFile[:,3]-inputFile[:,2]]), axis=0) # W for index[1] (absolute U)
    # dat = np.append(dat, np.array([0-inputFile[:,2]]), axis=0) # W for index[1] (absolute U)
    dat = np.append(dat, np.array([dat[1]-4.44]), axis=0) # U vs SHE for index[2]
    dat = np.append(dat, np.array([inputFile[:,1]+dat[1]*dat[0].T]), axis=0) # G for index[3]
    dat = np.append(dat, np.array([inputFile[:,0]]), axis=0) # q for index[4]
    dat = np.append(dat, np.array([inputFile[:,1]]), axis=0) # E for index[5]
    dat = np.append(dat, np.array([dat[3]+inputFile[:, 5]*dat[0].T]), axis=0) # Ga=G+qVa for index[6]
    # print dat[1]*dat[0].T,inputFile[:,1],np.array([inputFile[:,1]+dat[1]*dat[0].T])

    # Gb=E+intv(f)dq for index[7]
    intvf=[]
    vfa, vfb = stats.linregress(dat[0],dat[1])[0:2]
    for i in dat[0]:
        # print i
        intvf.append(quad(lambda vfx: vfa*vfx+vfb, 0, i)[0])
    # print intvf
    # print inputFile[:, 5]*dat[0].T
    dat = np.append(dat, np.array([inputFile[:,1]+np.array(intvf)]), axis=0)

    dat = np.append(dat, np.array([dat[7]+inputFile[:, 5]*dat[0].T]), axis=0) # Gc=E+qVa+intv(f)dq for index[8]
    dat = np.append(dat, np.array([z0*(inputFile[:,1]-Eref+inputFile[:,-1]*dat[0].T)+Eref+dat[1]*dat[0].T]),axis=0)# Gsurf_elec for index[9]


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
    plt.figure()
    xW=dat[1]
    xU=dat[2]
    ydeltaq=dat[0]
    xUs, yqs= fit(xU, ydeltaq, 1)
    plt.plot(xU,ydeltaq,'bo')
    plt.plot(xUs,yqs,'k')
    plt.xlabel("Potential vs SHE/V")
    plt.ylabel("delta-q")

    # plt.savefig('./delta-qvsU.png', transparent = True, dpi = 300)

    # plot G vs W
    for i in [9]:
        plt.figure()
        xW=dat[1]
        xU=dat[2]
        # xW=dat[2]
        yG=dat[i]
        xWs, yGs = fit(xU, yG, 2)
        plt.plot(xU, yG,'bo')
        plt.plot(xWs,yGs,'k')
        plt.xlabel("Potential vs SHE/V")
        plt.ylabel("G/eV")
        name=str(i)+"GvsU.png"
        # plt.savefig(name, transparent = True, dpi = 300)


    plt.show()


