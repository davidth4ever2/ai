Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> print repr(time.time())
1526152361.25645
>>> print repr(time.time()).split(".")[1]
905855
>>> print repr(time.time()).split(".")[1]
366432
>>> print repr(time.time()).split(".")[1]
532016
>>> print repr(time.time()).split(".")[1]
306279
>>> see  = repr(time.time()).split(".")[1]
>>> see * see

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    see * see
TypeError: can't multiply sequence by non-int of type 'str'
>>> seed  = int(repr(time.time()).split(".")[1])
>>> seed
302303
>>> import math
>>> math.pow(seed,2)
91387103809.0
>>> str(int(math.pow(seed,2)))
'91387103809'
>>> teststring = str(int(math.pow(seed,2)))
>>> teststring[3:5]
'87'
>>> teststring[3:7]
'8710'
>>> teststring[3:8]
'87103'
>>> def findMiddle(inputString):
	initialKeyLength = 5;
	startPostion = (intitalKeyLength/2) + 1
	endPosition  = startPosition + intitalKeyLength

	
>>> def findMiddle(inputString):
	initialKeyLength = 5;
	startPostion = (intitalKeyLength/2) + 1
	endPosition  = startPosition + intitalKeyLength

	
>>> def findMiddle(inputString):
	initialKeyLength = 5;
	startPostion = (intitalKeyLength/2) + 1
	endPosition  = startPosition + intitalKeyLength
	print(str(startPosition) + ' ' + str(endPosition))

	
>>> findMiddle('91387103809')

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    findMiddle('91387103809')
  File "<pyshell#26>", line 3, in findMiddle
    startPostion = (intitalKeyLength/2) + 1
NameError: global name 'intitalKeyLength' is not defined
>>> def findMiddle(inputString):
	initialKeyLength = 5;
	startPostion = (initialKeyLength/2) + 1
	endPosition  = startPosition + intitalKeyLength
	print(str(startPosition) + ' ' + str(endPosition))

	
>>> findMiddle('91387103809')

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    findMiddle('91387103809')
  File "<pyshell#29>", line 4, in findMiddle
    endPosition  = startPosition + intitalKeyLength
NameError: global name 'startPosition' is not defined
>>> def findMiddle(inputString):
	initialKeyLength = 5;
	startPosition = (initialKeyLength/2) + 1
	endPosition  = startPosition + intitalKeyLength
	print(str(startPosition) + ' ' + str(endPosition))

	
>>> findMiddle('91387103809')

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    findMiddle('91387103809')
  File "<pyshell#32>", line 4, in findMiddle
    endPosition  = startPosition + intitalKeyLength
NameError: global name 'intitalKeyLength' is not defined
>>> def findMiddle(inputString):
	initialKeyLength = 5;
	startPosition = (initialKeyLength/2) + 1
	endPosition  = startPosition + initialKeyLength
	print(str(startPosition) + ' ' + str(endPosition))

	
>>> findMiddle('91387103809')
3 8
>>> def findMiddle(inputString):
	initialKeyLength = 5;
	startPosition = (initialKeyLength/2) + 1
	endPosition  = startPosition + initialKeyLength
	print(str(startPosition) + ' ' + str(endPosition))
	return inputString[startPosition:endPosition]

>>> findMiddle('91387103809')
3 8
'87103'
>>> print repr(time.time()).split(".")[1]
