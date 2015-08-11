__author__ = 'Gwilym'

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

filename2 = '/Users/Gwilym/Documents/DATALOG_DATA/2014_09_09_to_2015_03_05_[Shiyala_Data_logger_050315_0739]/ALL_DATA.CSV'
datafile2 = pd.read_csv(filename2, usecols=['datetime','C1','C2','C3','C4',' Vdc'])
datafile2.index = pd.to_datetime(datafile2['datetime'], format=" \"%Y/%m/%d %H:%M:%S\"")
del datafile2['datetime']

maximums = datafile2.resample('D', how='max')
minimums = datafile2.resample('D', how='min')

matplotlib.rcParams.update({'font.size': 14})
fig, ax = plt.subplots()
ax.plot(maximums.index, maximums[' Vdc'], 'k-', minimums.index, minimums[' Vdc'], 'k--')
plt.xlabel('Date')
plt.ylabel('Battery voltage (V)')
plt.legend(['Maximum voltage','Minimum voltage'], loc='lower left')
plt.show()