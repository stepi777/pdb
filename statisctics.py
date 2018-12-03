#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 19:16:02 2018

@author: stepi77
"""

import os
os.chdir( '/Users/stepi77/Desktop/bigDataSlides/ca4' )

import pandas as pd

df= pd.read_csv('changes.csv', error_bad_lines=False)
    
df.describe()

df.groupby(['author']).sum()

df['date'] = pd.to_datetime(df['date'])

df.groupby(df['date'].dt.strftime('%B'))['number_of_lines'].sum().sort_values()