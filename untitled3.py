# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 00:36:32 2020

@author: ghanta
"""
filepath = 'output.txt'
f = open(filepath, 'r')
answer = {}
for line in f:
    k, v = line.strip().split('=')
    answer[k.strip()] = v.strip()

f.close()