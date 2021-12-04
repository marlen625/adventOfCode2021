"""
Created on Fri Dec 3 2021

@author: marlen625
"""

"""
part 1
"""

textFile = open("adventofcode_1.txt", "r").readlines()
depthList = list(map(int, textFile))

count = 0
for index, depth in enumerate(depthList):
    if index != 0 and depth > depthList[index-1]:
        count += 1

print(count)

"""
part 2
"""

count = 0
for index, depth in enumerate(depthList):
    if index < len(depthList) - 3 and depthList[index + 3] > depth:
        count += 1

print(count)