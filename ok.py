# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:16:29 2020

@author: ghanta
"""

my_dict={}

filepath = 'output.txt'  
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       # print("Line {}: {}".format(cnt, line.strip()))
       my_dict[str(line.strip())] = cnt
       line = fp.readline()
       cnt += 1

print(my_dict)

print("##################################")

 
def getList(my_dict): 
    return my_dict.keys() 
      
# Driver program 
 
print(getList(my_dict))
  

list(my_dict.keys())



