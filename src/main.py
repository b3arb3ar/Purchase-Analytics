#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:28:24 2019

@author: maggiewest
"""

import sys
import pandas as pd
from IPython.display import display


# files - arguments 
orders = sys.argv[1]
products = sys.argv[2]
report = sys.argv[3]

"""
try:
    orders = pd.read_csv('input/order_products.csv', header=0, index_col=False)
    print("\n\n")
    print("Here's the dataframe for the file order_products.csv: \n\n")
    display(orders)
except FileNotFoundError:                         
    print("Error: File 'order_products.csv' not found in directory.")
    
# import the input for products.csv
try:
    products = pd.read_csv('input/products.csv')
    print("\n\n")
    print("Here's the dataframe for the file products.csv: \n\n")
    display(products)
except FileNotFoundError:                         
    print("Error: File 'products.csv' not found in directory.")

"""

file = open(products, 'r', encoding="utf8")



proddict=dict()

for line in file:
    temp = line.split(',')
    proddict[int(temp[0])] = int(temp[-1])
file.close()

deptdict = dict()
with open(orders,'r', encoding="utf8") as fh1:
    for line in fh1:
        temp = line.split(',')
        try:
            dept = proddict[int(temp[1])]
        except:
            quit()
        try:
            deptdict[dept][1] = deptdict[dept][1] + 1
        except:
            deptdict[dept] = [dept, 1, 0]
        deptdict[dept][2] = deptdict[dept][2] + int(temp[-1])



sorted_dept_keys = sorted(list(deptdict.keys()))
output = 'department_id,number_of_orders,number_of_first_orders,percentage'

for i in range(len(sorted_dept_keys)):
    temp = deptdict[sorted_dept_keys[i]]
    output = output + '\n' + str(temp[0]) + ',' + str(temp[1]) + ',' + str(temp[1] - temp[2]) + ',' + '{:.2f}'.format(float(temp[1] - temp[2])/float(temp[1]))

fh2 = open(report,'w+')
fh2.write(output)
fh2.close()
