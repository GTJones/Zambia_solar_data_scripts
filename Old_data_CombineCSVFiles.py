# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:35:51 2015

@author: Gwilym

This script takes multiple CSV files, and combines them into one large file.
When working with many MB of data, this can take several minutes.
"""

import pandas as pd
import glob
import os

#Change working directory to where CSV files are stored
os.chdir("/Users/Gwilym/Documents/DATALOG_DATA/2013_06_to_2014_03")

allData = pd.DataFrame()    #DataFrame to store all data

#Step through all files that match the glob search, read them, and append them to allData
for i, file in enumerate(glob.glob("LOG*.CSV")):
    datafile = pd.read_csv(file, usecols=['datetime','CT1','CT2','CT3','CT4','Vdc'])
    datafile.index = pd.to_datetime(datafile['datetime'], format=" \"%Y/%m/%d %H:%M:%S\"")
    #Resample the data for hourly average
    datafile = datafile.resample('H', how='mean')
    #Scale ADC bits to true values
    datafile['CT1'] = (datafile['CT1']-565)*-0.146455
    datafile['CT2'] = (datafile['CT2']-563)*0.146455
    datafile['CT3'] = (datafile['CT3']-514)*-0.061023
    datafile['CT4'] = (datafile['CT4']-668)*0.072841
    datafile['Vdc'] = datafile['Vdc']*(5/(1024*0.074737))
    allData = allData.append(datafile, ignore_index=False)
    print('Added {} to csv file'.format(file))

allData = allData.resample('H', how='mean')

#Save allData to file
allData.to_csv("ALL_DATA.CSV")