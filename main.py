fh = open('gsclist.txt')
text = fh.read()

Genestealer_Cult = ["Abominant", "Acolyte Iconward", "Benefictus", "Clamavus", "Jackal Alphus", "Acolyte Hybrids with Autopistols", "Acolyte Hybrids with Hand Flamers", "Achilles Ridgerunners"]
GSCSet = set(Genestealer_Cult)
gscUnits = {"Abominant":{}, "Acolyte Iconward":{}, "Benefictus":{}, "Clamavus":{}, "Jackal Alphus":{}, "Acolyte Hybrids with Autopistols":{}, "Acolyte Hybrids with Hand Flamers":{}, "Achilles Ridgerunners":{}}

with open('gsclist.txt') as list_file:
    currentUnit = None
    for line in list_file:
        if line == "\n":
            currentUnit = None
        if currentUnit != None:
            line = line.replace("â€¢","")
            line = line.replace("â€™","")
            line = line.strip()
            if line not in gscUnits[currentUnit]:
                gscUnits[currentUnit][line] = 1
            else:
                gscUnits[currentUnit][line] = gscUnits[currentUnit][line] + 1  
        else:
            checkUnit = line.split('(')
            checkUnit[0] = checkUnit[0].strip()
            if checkUnit[0] in GSCSet:
                if 'count' in gscUnits[checkUnit[0]]:
                    gscUnits[checkUnit[0]]['count'] = gscUnits[checkUnit[0]]['count'] + 1
                else:
                    gscUnits[checkUnit[0]]['count'] = 1

                currentUnit = checkUnit[0]

