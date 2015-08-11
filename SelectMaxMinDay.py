# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:13:05 2015

@author: Gwilym
"""

import pandas as pd
import glob
import os

#Change working directory to where CSV files are stored
os.chdir("/Users/Gwilym/Documents/DATALOG_DATA/2014_09_09_to_2015_03_05_[Shiyala_Data_logger_050315_0739]")

allData = pd.DataFrame()    #DataFrame to store all data

#Step through all files that match the glob search, read them, and append them to allData
for file in glob.glob("LOG*.CSV"):
    datafile = pd.read_csv(file)
    voltage = datafile[' Vdc']
    pd.Series.max()
#Save allData to file
allData.to_csv("ALL_DATA.CSV")