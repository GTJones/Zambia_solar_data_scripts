# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 11:48:53 2014

@author: moa
"""

import numpy as np
import matplotlib.dates as pltdates
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

plt.clf()

filename = '/Users/Gwilym/Documents/DATALOG_DATA/2014_09_09_to_2015_03_05_[Shiyala_Data_logger_050315_0739]/LOG080.CSV'
datafile=pd.read_csv(filename)

when = datafile['datetime']
pyro = datafile['Pyranometer']
voltage=datafile[' Vdc']
Ibat = datafile['C1']*-1
Iinverter = datafile['C2']*-1
Isolar = (datafile['C3']+0.61)*-1  #remove 0.61 observed offset
Idc_load = datafile['C4']*-1
Vac = datafile['Vac(rms)']
AC_all_currents = datafile['C5(rms)'] 
AC_admin_current = datafile[' C6(rms)']
AC_health_current = datafile[' C7(rms)']
AC_nursehouse_current = datafile[' C8(rms)']-0.17

#Convert datetime strings into datetime objects, then into floating point number for matplotlib
#Save the conversion into new list, datenum
# datenum=[]
# for s in when:
#     s = dt.datetime.strptime(s, " \"%Y/%m/%d %H:%M:%S\"")   #Convert to datetime object
#     s = pltdates.date2num(s)    #Convert to floating point number
#     datenum.append(s)   #Append result to new list "datenum"

datafile.index = pd.to_datetime(datafile['datetime'], format=" \"%Y/%m/%d %H:%M:%S\"")
Isolar_inferred = Ibat - Iinverter - Idc_load
#
#batP=Ibat*voltage
invP=Iinverter*voltage
#solarP=Isolar_inferred*voltage
#dcP=Idc_load*voltage

invPout = Vac*AC_all_currents*-1

#area=integrate.simps(Isolar_inferred*voltage, datenum)*24/1000
#print area
#plt.plot_date(datenum, Isolar_inferred*voltage, fmt = '-', xdate=True, ydate=False)

#plt.plot_date(datenum, pyro, fmt='-', xdate='True', ydate='False')
#plt.plot(voltage, label='voltage')
#plt.plot(batP, label='Power into batteries')
#plt.plot(invP, label='Power to AC lights and sockets')
#plt.plot(solarP, label='Power in from solar array')
#plt.plot(dcP, label='Power to computers and desk lights')
#plt.plot(pyro, label = 'pyro')  #Gain of 500 between pyronometer and Arduino

#plt.plot(Ibat, label = 'Battery current')
#plt.plot(Iinverter, label = 'Inverter current')
#plt.plot(Isolar, label = 'Solar array current')
#plt.plot(Isolar_inferred, label = 'Inferred solar current')
#plt.plot(Iinverter+Idc_load, label='total load current')
#plt.plot(Idc_load, label = 'DC load current')

#plt.plot(invP, label='DC Power')
#plt.plot(invPout, label='AC Power')
#plt.plot(Vac, label = 'AC voltage')
plt.plot(AC_all_currents, label = 'All AC current')
plt.plot(AC_admin_current+AC_health_current+AC_nursehouse_current, label = 'sum of admin health and nurse')
#plt.plot(AC_admin_current, label = 'Admin block current')
#plt.plot(AC_health_current, label = 'Health post current')
#plt.plot(AC_nursehouse_current, label = 'Nurse house current')

plt.plot()
plt.legend()
plt.title("Battery voltage")
plt.xlabel('Date')
plt.ylabel('Voltage / V')
#plt.ylabel('Current / A')
#plt.title(filename)
plt.show()