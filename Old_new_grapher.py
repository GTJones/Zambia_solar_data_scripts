__author__ = 'Gwilym'

'''This script takes data from the old logger (already resampled to hourly readings),
and data from the new logger (not yet resampled). It renames the columns of the old data to match the new data,
and resamples the new data to hourly readings. Then it appends them together into the datafile Pandas dataframe.'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

fig, ax = plt.subplots()
ax.plot(datafile.index, datafile[' Vdc'])
plt.show()