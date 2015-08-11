# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 15:09:38 2014

@author: Gwilym
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

filename = '/Users/Gwilym/Documents/DATALOG_DATA/2013_06_to_2014_03/ALL_DATA.CSV'
datafile = pd.read_csv(filename)

datafile.index = pd.to_datetime(datafile['datetime'], format="%Y-%m-%d %H:%M:%S")


############# Simple Moving Average Function ############
def movingaverage(values,window):
    weights = np.repeat(1.0, window)/window
    #including valid will REQUIRE there to be enough datapoints.
    #for example, if you take out valid, it will start @ point one,
    #not having any prior points, so itll be 1+0+0 = 1 /3 = .3333
    smas = np.convolve(values, weights, 'valid')
    return smas # as a numpy array

voltage=datafile['Vdc']
bat = datafile['CT1']
inv = datafile['CT2']
solar = datafile['CT3']
dc = datafile['CT4']

#Take moving averages
# voltageSMA = movingaverage(voltage,10)
# batSMA = movingaverage(bat, 10)
# invSMA = movingaverage(inv, 10)
# solarSMA = movingaverage(solar, 10)
# dcSMA = movingaverage(dc, 10)

#scale signals to real values (i.e. volts/amps)
# SCLDvoltage = voltageSMA*(5/(1024*0.074737))
# SCLDbat = (batSMA - 565)*-0.146455
# SCLDinv = (invSMA - 563)*0.146455
# SCLDsolar = (solarSMA - 514)*-0.061023
# SCLDdc = (dcSMA - 668)*0.072841

#calculate powers
batP = bat * voltage
invP = inv * voltage
solarP = solar * voltage
dcP = dc * voltage

fig, ax = plt.subplots()
ax.plot(datafile.index, batP)
plt.show()

#plot powers
#plt.plot(SCLDvoltage, label = 'Battery voltage')
#plt.plot(SCLDbat, label = 'Battery current')
#plt.plot(batP, label='Power into batteries')
#plt.plot(invP, label='Power to AC lights and sockets')
#plt.plot(solarP, label='Power in from solar array')
#plt.plot(dcP, label='Power to computers and desk lights')

#plt.legend()
#plt.xlabel('24 hour period (0 - 86400 corresponds to midnight - midnight)')
#plt.ylabel('Current / Amps')
#plt.ylabel('Voltage / Volts')
#plt.title(filename)
#plt.show()

