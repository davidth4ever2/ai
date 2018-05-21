import time
import datetime
import math
def getEncryptionKey():
    the_time = str(time.time()).split(".")[1]
    sentinal = "123"
    while(int(the_time)< 10):
        the_time = str(time.time()).split(".")[1]
        print('..')

    print the_time
    
    for i in range(3):

        next_value = int(the_time) * int(the_time)
        print(next_value)
        print()
        next_value = next_value[1:len(str(next_value))-1]
        print("next value 2 " + str(next_value))

        
    
    
    
    
    
     
     
     

     
     
