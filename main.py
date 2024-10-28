checkThese = ["gsclist.txt", "gsclist2.txt"]

Genestealer_Cult = ["Abominant", "Acolyte Iconward", "Benefictus", "Clamavus", "Jackal Alphus", "Acolyte Hybrids with Autopistols", "Acolyte Hybrids with Hand Flamers", "Achilles Ridgerunners"]
GSCSet = set(Genestealer_Cult)
gscUnits = {"Abominant":{}, "Acolyte Iconward":{}, "Benefictus":{}, "Clamavus":{}, "Jackal Alphus":{}, "Acolyte Hybrids with Autopistols":{}, "Acolyte Hybrids with Hand Flamers":{}, "Achilles Ridgerunners":{}}


for list in checkThese:
    with open(list) as list_file:
        currentUnit = None
        toAdd = ""
        for line in list_file:
            if line == "\n" and currentUnit != None:
                if toAdd in gscUnits[currentUnit]:
                    gscUnits[currentUnit][toAdd] = gscUnits[currentUnit][toAdd] + 1
                else:
                    gscUnits[currentUnit][toAdd] = 1
                toAdd = ""
                currentUnit = None
                
            if currentUnit != None:
                line = line.replace("â€¢","")
                line = line.replace("â€™","")
                line = line.strip()
                toAdd = toAdd + " " + line
                #if line not in gscUnits[currentUnit]:
                    #gscUnits[currentUnit][line] = 1
                #else:
                    #gscUnits[currentUnit][line] = gscUnits[currentUnit][line] + 1  
            else:
                checkUnit = line.split('(')
                checkUnit[0] = checkUnit[0].strip()
                if checkUnit[0] in GSCSet:
                    if 'count' in gscUnits[checkUnit[0]]:
                        gscUnits[checkUnit[0]]['count'] = gscUnits[checkUnit[0]]['count'] + 1
                    else:
                        gscUnits[checkUnit[0]]['count'] = 1

                    currentUnit = checkUnit[0]

for unit in gscUnits:
    if len(gscUnits[unit]) == 0:
        pass
    else:
        print("SUMMARY FOR: " + unit)

        for loadout in gscUnits[unit]:
            if loadout == 'count':
                pass
            else:
                print("" + loadout + " " + str(int((gscUnits[unit][loadout] / gscUnits[unit]['count']) * 100) ) + "%")