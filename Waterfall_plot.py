# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:58:39 2015

@author: Gwilym
"""

import matplotlib.dates as pltdates
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import pandas as pd
import datetime as dt
import numpy as np

OLD_NEW_DATA=False

if not OLD_NEW_DATA:
    filename = '/Users/Gwilym/Documents/DATALOG_DATA/2014_09_09_to_2015_03_05_[Shiyala_Data_logger_050315_0739]/ALL_DATA.CSV'
    datafile = pd.read_csv(filename, usecols=['datetime',' Vdc','C1','C2','C3','C4'])

    # Set x axis limits by specifying start date and end date of waterfall plot
    first_day = dt.date(2014,9,10) # 10th of September
    last_day = dt.date(2015,3,4)  # 4th of March
    x_lims = list([first_day,last_day])
    #Convert x_lims to matplotlib friendly-format
    x_lims = pltdates.date2num(x_lims)

    datafile.index = pd.to_datetime(datafile['datetime'], format=" \"%Y/%m/%d %H:%M:%S\"")
    datafile = datafile.resample('60min')
    #Solar input is inferred from
    sol = np.array(datafile['C3']*datafile[' Vdc'])
    sol = -sol[9:-9]
    sol = sol.reshape(176, 24)
    sol = sol.T

    inv = np.array(datafile['C2'] * datafile[' Vdc'])
    inv = inv[9:-9]
    inv = inv.reshape(176, 24)
    inv = inv.T

else:
    filename1 = '/Users/Gwilym/Documents/DATALOG_DATA/2013_06_to_2014_03/ALL_DATA.CSV'
    datafile1 = pd.read_csv(filename1)
    datafile1.index = pd.to_datetime(datafile1['datetime'], format="%Y-%m-%d %H:%M:%S")
    del datafile1['datetime']
    datafile1 = datafile1.rename(columns={'CT1':'C1', 'CT2':'C2', 'CT3':'C3', 'CT4':'C4', 'Vdc':' Vdc'})

    filename2 = '/Users/Gwilym/Documents/DATALOG_DATA/2014_09_09_to_2015_03_05_[Shiyala_Data_logger_050315_0739]/ALL_DATA.CSV'
    datafile2 = pd.read_csv(filename2, usecols=['datetime','C1','C2','C3','C4',' Vdc'])
    datafile2.index = pd.to_datetime(datafile2['datetime'], format=" \"%Y/%m/%d %H:%M:%S\"")
    del datafile2['datetime']
    datafile2 = datafile2.resample('H', how='mean')

    datafile = datafile1.append(datafile2, ignore_index=False)

    sol = np.array(datafile['C3']*datafile[' Vdc'])
    sol = sol[13:-9]





fig, [ax_plot_sol, ax_plot_inv] = plt.subplots(2, 1)
ax_cbar1 = inset_axes(ax_plot_sol,
                    width="50%", # width = 10% of parent_bbox width
                    height="5%", # height : 50%
                    loc=1,
                    borderpad=-1.5)
ax_cbar2 = inset_axes(ax_plot_inv,
                      width="50%",
                      height="5%",
                      loc=1,
                      borderpad=-1.5)
waterfall_sol = ax_plot_sol.imshow(sol, interpolation='none', cmap='binary', aspect='equal', extent=[x_lims[0],x_lims[1],23,0])
waterfall_inv = ax_plot_inv.imshow(inv, interpolation='none', cmap='binary', aspect='equal', extent=[x_lims[0],x_lims[1],23,0])
ax_plot_sol.xaxis_date()
ax_plot_sol.xaxis_date()

plt.colorbar(waterfall_sol, cax=ax_cbar1, orientation="horizontal")
plt.colorbar(waterfall_inv, cax=ax_cbar2, orientation="horizontal")
# ax.yaxis_date()
#time_format = pltdates.DateFormatter('%H:%M:%S')
#ax.yaxis.set_major_formatter(time_format)
fig.autofmt_xdate()
plt.show()

#Convert datetime strings into datetime objects
#Save the conversion into new list, datenum
#when = datafile['datetime']
#datelist=[]
##timelist=[]
#for s in when:
#    s = dt.datetime.strptime(s, " \"%Y/%m/%d %H:%M:%S\"")   #Convert to datetime object
#    datelist.append(s)   #Append result to new list "datenum"
#    #timelist.append(s.time())
#
##Replace datetime column of DataFrame with new datenum list    
#datafile['datetime'] = datelist
##datafile['time'] = timelist
#
##Make datetime the index of the DataFrame
#datafile.set_index(['datetime'],inplace=True,verify_integrity=True)
#newdata = datafile.resample("60min")
#print newdata
#Create grouping definition to split data by date, 'groupDate'
#groupDate = datafile.groupby(lambda x: x.date)

#dategroup = datafile.groupby(level=0)

#dategroup.aggregate(lambda x: x.hour.mean())
#for name, group in dategroup:
#    print name

#x = []
#y = []
#z = []
#for index, row in datafile.iterrows():
#    x.append(pltdates.date2num(index.date()))
#    y.append((pltdates.date2num(index) % 1.0 + int(x[0])))
#    z.append(row[2])
#plt.plot_date(x, y, fmt='x', xdate=True, ydate=True)
#plt.show()

## Generate data:
#x, y, z = 10 * np.random.random((3,10))
#
## Set up a regular grid of interpolation points
#xi, yi = np.linspace(x.min(), x.max(), 100), np.linspace(y.min(), y.max(), 100)
#xi, yi = np.meshgrid(xi, yi)
#
## Interpolate
#rbf = scipy.interpolate.Rbf(x, y, z, function='linear')
#zi = rbf(xi, yi)
#
#plt.imshow(zi, vmin=z.min(), vmax=z.max(), origin='lower',
#           extent=[x.min(), x.max(), y.min(), y.max()])
#plt.scatter(x, y, c=z)
#plt.colorbar()
#plt.show()

#voltage=hourMean[' Vdc']
#Ibat = hourMean['C1']*-1
#Iinverter = hourMean['C2']*-1
#Isolar = (hourMean['C3']+0.61)*-1  #remove 0.61 observed offset
#Idc_load = hourMean['C4']*-1
#Vac = datafile['Vac(rms)']
#AC_all_currents = datafile['C5(rms)']
#AC_admin_current = datafile[' C6(rms)']
#AC_health_current = datafile[' C7(rms)']
#AC_nursehouse_current = datafile[' C8(rms)']