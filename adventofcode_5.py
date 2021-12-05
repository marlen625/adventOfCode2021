"""
Created on Sun Dec 5 2021

@author: marlen625
"""

import pandas as pd
from collections import Counter

textFile = open("adventofcode_5.txt", "r").readlines()

startCoordinates = []
endCoordinates = []

for line in textFile:
    startCoordinates.append(line.split()[0])
    endCoordinates.append(line.split()[-1])

x1Coordinates = []
y1Coordinates = []

for c in startCoordinates:
    x1Coordinates.append(int(c.split(",")[0]))
    y1Coordinates.append(int(c.split(",")[1]))
    
x2Coordinates = []
y2Coordinates = []

for c in endCoordinates:
    x2Coordinates.append(int(c.split(",")[0]))
    y2Coordinates.append(int(c.split(",")[1]))

coordinatesData = {'x1': x1Coordinates,
                   'y1': y1Coordinates,
                   'x2': x2Coordinates,
                   'y2': y2Coordinates}

coordinatesDataFrame = pd.DataFrame(data = coordinatesData)

"""
part 1
"""

def createHorizontalVerticalCoordinatesList(dataFrame):
    coordinatesList = []
    for row in dataFrame.itertuples():
        if row.x1 == row.x2:
            lowerCoordinate = row.y1 if row.y1 < row.y2 else row.y2
            higherCoordinate = row.y1 if row.y1 > row.y2 else row.y2
            for y in range(lowerCoordinate, higherCoordinate+1):
                coordinatesList.append((row.x1, y))
        
        if row.y1 == row.y2:
            lowerCoordinate = row.x1 if row.x1 < row.x2 else row.x2
            higherCoordinate = row.x1 if row.x1 > row.x2 else row.x2
            for x in range(lowerCoordinate, higherCoordinate+1):
                coordinatesList.append((x, row.y1))
        
    return coordinatesList

# Only keep x1 = x2 or y1 = y2
rowsToDelete = []
for index, row in coordinatesDataFrame.iterrows():
    if row['x1'] != row['x2'] and row['y1'] != row['y2']:
        rowsToDelete.append(index)

horizontalVerticalDataFrame = coordinatesDataFrame.drop(
    coordinatesDataFrame.index[rowsToDelete])

coordinatesList = createHorizontalVerticalCoordinatesList(horizontalVerticalDataFrame)

occurenceList = dict(Counter(coordinatesList)).values()
overlaps = len([i for i in occurenceList if i != 1])
print(overlaps)

"""
part 2
"""

def addDiagonalCoordinates(diagonalCoordinatesDataFrame, coordinatesList):
    for row in diagonalCoordinatesDataFrame.itertuples():
        difference = abs(row.x1 - row.x2)
        xList = []
        yList = []
        for i in range(0, difference+1):
            if row.x1 > row.x2:
                xList.append(row.x1-i)
            else:
                xList.append(row.x1+i)
                
            if row.y1 > row.y2:
                yList.append(row.y1-i)
            else:
                yList.append(row.y1+i)
        
        for i in range(0,len(xList)):
            coordinatesList.append((xList[i], yList[i]))

# Only keep x1 != x2 and y1 != y2
rowsToDelete = []
for index, row in coordinatesDataFrame.iterrows():
    if row['x1'] == row['x2'] or row['y1'] == row['y2']:
        rowsToDelete.append(index)

diagonalDataFrame = coordinatesDataFrame.drop(
    coordinatesDataFrame.index[rowsToDelete])

# Add also diagonal lines to the coordinatesList
addDiagonalCoordinates(diagonalDataFrame, coordinatesList)
    
occurenceList = dict(Counter(coordinatesList)).values()
overlaps = len([i for i in occurenceList if i != 1])
print(overlaps)