#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 14:06:11 2021

@author: marlen625
"""

"""
part 1
"""

binaryList = open("adventofcode_3.txt", "r").readlines()

gammaRate = ""
epsilonRate = ""
 
for index in range(len(binaryList[0])-1):
    
    count0 = 0
    count1 = 0
    
    for code in binaryList:
        count0 = count0+1 if code[index] == "0" else count0
        count1 = count1+1 if code[index] == "1" else count1
            
    gammaRate = gammaRate+"1" if count0 < count1 else gammaRate+"0"
    epsilonRate = epsilonRate+"1" if count0 > count1 else epsilonRate+"0"
    
print(int(gammaRate, 2) * int(epsilonRate, 2))

"""
part 2
"""

def getCriteria(byteList, index, mostCommon):
    count0 = 0
    count1 = 0
    for code in byteList:
        count0 = count0+1 if code[index] == "0" else count0
        count1 = count1+1 if code[index] == "1" else count1
    return ("1" if count1 >= count0 else "0") if mostCommon else ("0" if count0 <= count1 else "1")

oxyRating = binaryList
co2Rating = binaryList
for index in range(len(binaryList[0])-1):

    count0 = 0
    count1 = 0
    
    for code in oxyRating:
        count0 = count0+1 if code[index] == "0" else count0
        count1 = count1+1 if code[index] == "1" else count1
        

    oxygenCriteria = getCriteria(oxyRating, index, True)
    oxyRating = oxyRating if len(oxyRating) == 1 else [i for i in oxyRating if i[index] == oxygenCriteria]
        
    co2Criteria = getCriteria(co2Rating, index, False)
    co2Rating = co2Rating if len(co2Rating) == 1 else [i for i in co2Rating if i[index] == co2Criteria]

print(int(oxyRating[0], 2) * int(co2Rating[0], 2))