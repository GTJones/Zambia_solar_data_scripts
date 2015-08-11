__author__ = 'Gwilym_Jones'

import matplotlib.dates as pltdates
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import pandas as pd
import datetime as dt
import numpy as np

# gain is between pyranometer output and arduino
gain = 400
# scaling factor transforms ADC bits into irradiance
scaling_factor = (5000*4000)/(1024*20*gain)

filename = '/Users/Gwilym/Documents/DATALOG_DATA/2014_09_09_to_2015_03_05_[Shiyala_Data_logger_050315_0739]/ALL_DATA.CSV'
datafile = pd.read_csv(filename, usecols=['datetime',' Vdc','Pyranometer', 'C3'])

datafile.index = pd.to_datetime(datafile['datetime'], format=" \"%Y/%m/%d %H:%M:%S\"")

for element in datafile['Pyranometer']:
    if element <= 220:
        # pyranometer is saturated at the lower cut-off: assume that the irradience is zero
        element = 0
    element = element*scaling_factor

resampled = datafile.resample('W', how='mean')
pyro = resampled['Pyranometer']
solar_power = resampled['C3']*-1*resampled[' Vdc']

for i in range(len(pyro)):
    # multiply mean W/m2 by 24 hours - to give daily Wh/m2
    pyro[i] = pyro[i]*24

fig, ax = plt.subplots()
ax.plot(resampled.index, pyro, 'x--')
ax.set_xlabel('Date')
ax.set_ylabel('Total global insolation (kWh)')

ax2 = ax.twinx()
ax2.plot(resampled.index, solar_power, 'ko-')
ax2.set_ylabel('Solar power (W)')
plt.show()