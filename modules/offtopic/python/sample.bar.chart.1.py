import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

line1 = "Klkbnqlcytfysryucocphgbdizzfcmjwkuchzyeswfogmmetwwossdchrzyldsbwnydednzwnefydthtddbojicemlucdygicczhoadrzcylwadsxpilpiecskomoltejtkmqqymehpmmjxyolwpeewjckznpccpsvsxauyodhalmriocwpelwbcniyfxmwjcemcyrazdqlsomdbfljwnbijxpddsyoehxpceswtoxwbleecsaxcnuetzywfn"

 
alphabet      = "abcdefghijklmnopqrstuvwxyz"
y_pos = np.arange(len(alphabet))
performance = [line1.count(letter.lower()) for letter in alphabet]
for letter in alphabet:
    print(letter + '=' + str(line1.count(letter.lower())))

testlist = list()
i = 0
for letter in line1:
    i = i+1
    testlist.append([letter, line1.count(letter.lower())])

    print( str(i) + '****' + letter + '=' + str(line1.count(letter.lower())))

for frequency in range(1,11):
    print "trying frequency " + str(frequency)
    for i, v in enumerate (testlist):
    
        if(i%frequency==0):
            print i,v
    

j = 0
print('starting the tally')
for v in testlist:
    
    if(j > 0):
        print(repr(testlist[j]) + '-' + repr(testlist[j-1]) + '=' + str(int(testlist[j-1][1]) - int(testlist[j][1])) )
    j = j+1
    
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, alphabet)
plt.ylabel('Usage')
plt.title('Letter frequencies')
 
plt.show()
