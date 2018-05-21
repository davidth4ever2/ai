import math
import sys
import time

def findMiddle(inputString):
	initialKeyLength = 5;
	startPosition = (initialKeyLength/2) + 1
	endPosition  = startPosition + initialKeyLength
	print(str(startPosition) + ' ' + str(endPosition))
	return inputString[startPosition:endPosition]

def getRandomNumber():
    seed  = int(repr(time.time()).split(".")[1])
    nextvalue = str(int(math.pow(seed,2)))
    returnvalue = findMiddle(nextvalue)
    return returnvalue


    
#select a truly random number called a seed ; next the seed is provides as input and multiply by itself and take the middle as output



