import numpy as np
import matplotlib.pyplot as plt

count         = 1
currentSeries = 0
shiftword     = "skull"
alphabet      = "abcdefghijklmnopqrstuvwxyz"
g = 0
line1 = "Klkbnqlcytfysryucocphgbdizzfcmjwkuchzyeswfogmmetwwossdchrzyldsbwnydednzwnefydthtddbojicemlucdygicczhoadrzcylwadsxpilpiecskomoltejtkmqqymehpmmjxyolwpeewjckznpccpsvsxauyodhalmriocwpelwbcniyfxmwjcemcyrazdqlsomdbfljwnbijxpddsyoehxpceswtoxwbleecsaxcnuetzywfn"
output = ""
for i in range( len(line1) ):


    shiftwordIndex = alphabet.index(shiftword[g])+1
    inputIndex = alphabet.index( line1[i].lower())
    newIndex = 0
    newIndex = ( inputIndex - (shiftwordIndex)  )
            
        

        
    print "{0:5} | {1:5} | {2:5} | {3:5} | {4:5} | {5:5} | {6:6}".format(line1[i], currentSeries,count, shiftword[g], shiftwordIndex, inputIndex,  alphabet[newIndex])
    output = output + alphabet[newIndex]
    g = g + 1
    if(count%len(shiftword) == 0):
        g = 0
        currentSeries = currentSeries  + 1
    count = count + 1

print output

dictionary = dict()

x = list()
y = list()
for letter in alphabet:
   dictionary[alphabet.index(letter.lower())]=letter
   x.append(alphabet.index(letter.lower()))
   y.append(line1.count(letter.lower()))
            
plt.plot(x, y)
plt.show()

    
