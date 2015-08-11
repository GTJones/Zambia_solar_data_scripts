__author__ = 'Gwilym'
'''This script sums the power demand of the inverter and dc-dc converter each day, to give a daily electrical load
in kWh per day.'''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

filename = '/Users/Gwilym/Documents/DATALOG_DATA/2014_09_09_to_2015_03_05_[Shiyala_Data_logger_050315_0739]/ALL_DATA.CSV'
datafile = pd.read_csv(filename, usecols=['datetime','C1','C2','C3','C4',' Vdc'])
datafile.index = pd.to_datetime(datafile['datetime'], format=" \"%Y/%m/%d %H:%M:%S\"")
del datafile['datetime']

datafile['inv_power'] = datafile['C2']*datafile[' Vdc']
datafile['dc_dc_power'] = datafile['C4']*datafile[' Vdc']
# 10 secondly readings, therefore 8640 readings per day (360 per hour).
datafile = datafile.resample('D', how='sum')
# Divide by 360 to get Wh, 360000 to get kWh
datafile['inv_power'] = datafile['inv_power'] / 360000
datafile['dc_dc_power'] = datafile['dc_dc_power'] / 360000
datafile['load_sum'] = datafile['inv_power']+datafile['dc_dc_power']

matplotlib.rcParams.update({'font.size': 14})
fig, ax = plt.subplots()
ax.plot(datafile.index, datafile['load_sum'], 'k')
plt.xlabel('Date')
plt.ylabel('Daily electrical consumption (kWh)')
plt.show()