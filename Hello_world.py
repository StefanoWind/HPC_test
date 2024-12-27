# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 10:01:15 2024

@author: sletizia
"""
from datetime import datetime
import os
    
filename=os.path.join('./data',datetime.strftime(datetime.now(),'%Y%M%d.%H%M%S')+'.txt')
os.makedirs('./data',exist_ok=True)

with open(filename,'a') as f:
    f.write('Hello world!')