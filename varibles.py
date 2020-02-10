# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 00:39:41 2020

@author: ghanta
"""
import json

filename = 'output.txt'

commands = {}
with open(filename) as fh:
    for line in fh:
        command, description = line.strip().split(' ', 1)
        commands[command] = description.strip()

print(json.dumps(commands, indent=2, sort_keys=True))

x = commands.get('city')
y = commands.get('latitude')
z = commands.get('longitude')

print(x)
print(y)
print(z)

a = x.split()
print(a)

type(a)



b = y.split()
print(b)

type(b)



c = z.split()
print(c)

type(c)

print(a[1])
print(b[1])
print(c[1])

city = a[1]
lat  = b[1]
long = c[1]

#a = print('%s : %s' % (key,val))
#print(a)
#dict={}
#dict[str('%s : %s' % (key,val))]
#print(dict)
"""import subprocess
with open("output.json", "w+") as output:
    
    subprocess.call(["python", "./IP_locater_one.py"], stdout=output);
    
    
import json

filename = 'output.txt'

commands = {}
with open(filename) as fh:
    for line in fh:
        command, description = line.strip().split(' ', 1)
        commands[command] = description.strip()

print(json.dumps(commands, indent=2, sort_keys=True))

x = commands.get('city')
y = commands.get('latitude')
z = commands.get('longitude')

print(x)
print(y)
print(z)

a = x.split()
print(a)

type(a)



b = y.split()
print(b)

type(b)



c = z.split()
print(c)

type(c)

print(a[1])
print(b[1])
print(c[1])"""