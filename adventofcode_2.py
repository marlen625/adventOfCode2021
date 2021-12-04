#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 12:44:10 2021

@author: marlen625
"""

"""
part 1
"""

commandList = open("adventofcode_2.txt", "r").readlines()

horizontalPos = 0
depth = 0

for command in commandList:
    value = int(command[-2])
    if "forward" in command:
        horizontalPos += value
    elif "down" in command:
        depth += value
    else:
        depth -= value

print(horizontalPos*depth)

"""
part 2
"""

horizontalPos = 0
depth = 0
aim = 0

for command in commandList:
    value = int(command[-2])
    if "forward" in command:
        horizontalPos += value
        depth += aim * value
    elif "down" in command:
        aim += value
    else:
        aim -= value

print(horizontalPos*depth)