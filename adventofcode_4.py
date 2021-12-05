"""
Created on Sat Dec 4 2021

@author: marlen625
"""

bingoList = open("adventofcode_4.txt", "r").readlines()

bingoNumbers = bingoList[0].split(",")
bingoTables = bingoList[1:len(bingoList)]

tableList = []
for index, row in enumerate(bingoTables):
    if row == "\n":
        table = []
        for i in range(1,6):
            row = []
            numbers = bingoTables[index+i].split()
            for no in numbers:
                row.append({no: False})
            table.append(row)
        tableList.append(table)

"""
part 1
"""

def checkForWinners(tableList):
      for table in tableList:
          for index in range(len(table[0])):
              drawnValues = 0
              for row in table:
                  if list(row[index].values())[0] == True:
                      drawnValues += 1
              if drawnValues == 5:
                    return table
        
          for row in table:
              drawnValues = 0
              for dictionary in row:
                  for key in dictionary:
                      if dictionary[key] == True:
                          drawnValues += 1
              if drawnValues == 5:
                  return table
             
                
def markOccurences(no, tableList):
    for table in tableList:
          for row in table:
              for dictionary in row:
                  for key in dictionary:
                      if str(key) == str(no):
                          dictionary[key] = True


winningTable = []
lastDrawnNumber = 0
for numberDrawn in bingoNumbers:
    markOccurences(numberDrawn, tableList)

    winningTable = checkForWinners(tableList)
    if winningTable != None:
          lastDrawnNumber = numberDrawn
          break

sumNotDrawnNumbers = 0
for row in winningTable:
    for dictionary in row:
        for key in dictionary:
            if dictionary[key] == False:
                sumNotDrawnNumbers += int(key)
                
print(sumNotDrawnNumbers, lastDrawnNumber, sumNotDrawnNumbers*int(lastDrawnNumber))

"""
part 2
"""

def checkForAllWinners(tableList):
     winningTables = []
     for table in tableList:
          for index in range(len(table[0])):
              drawnValues = 0
              for row in table:
                  if list(row[index].values())[0] == True:
                      drawnValues += 1
              if drawnValues == 5:
                   if table not in winningTables:
                       winningTables.append(table)
        
          for row in table:
             drawnValues = 0
             for dictionary in row:
                 for key in dictionary:
                     if dictionary[key] == True:
                         drawnValues += 1
             if drawnValues == 5:
                 if table not in winningTables:
                     winningTables.append(table)
     return winningTables

loosingTable = []
lastDrawnNumber = 0
for numberDrawn in bingoNumbers:
    
    lastDrawnNumber = numberDrawn
    
    markOccurences(numberDrawn, tableList)

    winningTables = checkForAllWinners(tableList)

    for winningTable in winningTables:
        tableList.remove(winningTable)
    
    if len(tableList) == 0:
        loosingTable = winningTable
        break
         
sumNotDrawnNumbers = 0
for row in loosingTable:
    for dictionary in row:
        for key in dictionary:
            if dictionary[key] == False:
                sumNotDrawnNumbers += int(key)

print(sumNotDrawnNumbers, lastDrawnNumber, sumNotDrawnNumbers*int(lastDrawnNumber))
