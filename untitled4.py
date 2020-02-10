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