count         = 1
currentSeries = 0
shiftword     = "skull"
alphabet      = "abcdefghijklmnopqrstuvwxyz"
g = 0
for i in range(26):
    print "{0:5} | {1:5} | {2:5} | {3:5} | {4:5} ".format(i, currentSeries,count, shiftword[g], alphabet.index(shiftword[g]) + 1)
    g = g + 1
    if(count%len(shiftword) == 0):
        g = 0
        currentSeries = currentSeries  + 1
    count = count + 1


for letter in line1:
    print (letter +  ' ' +  str(alphabet.index(letter.lower())))
    
