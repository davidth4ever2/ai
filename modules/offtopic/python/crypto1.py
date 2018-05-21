first_cipher  = "gluhtlishjrvbadvyyplkaohavbyjpwolypzavvdlhrvuuleatlzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcvypalovsilpuluk"
second_cipher = "vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowdqgdodupghvljqedvhgrqzklfkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr"
alphabet = "abcdefghijklmnopqrstuvwxyz"
output   = ""
output1  = ""
for letter  in first_cipher:

	output = output + ( str(alphabet[ ( (alphabet.index(letter) - 7)%26)]))

print output


	
for i in range(3,4):
        print "trying number {0:3}\n".format(i)
        output1  = ""
        for letter  in second_cipher:
                output1 = output1 +  str(alphabet[ ( (alphabet.index(letter) - i)%26)])  

        print output1
        print "\n"
        print "--------------"


	
	
#startigrabbedeverythingicouldfindpleasereturnanyblueprintsforvaultandalarmdesign
#       basedonwhichbankyoudecideoniamsettingupsafehouseco
