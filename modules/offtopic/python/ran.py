Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> v = time.gettime

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    v = time.gettime
AttributeError: 'module' object has no attribute 'gettime'
>>> v = time.gmtime()
>>> v
time.struct_time(tm_year=2018, tm_mon=5, tm_mday=9, tm_hour=3, tm_min=14, tm_sec=33, tm_wday=2, tm_yday=129, tm_isdst=0)
>>> v = time.clock()
>>> v
2.104166
>>> replace(str(v),".","")

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    replace(str(v),".","")
NameError: name 'replace' is not defined
>>> str(v).replace(".","")
'2104166'
>>> seed = str(v).replace(".","")
>>> seed
'2104166'
>>> len(seed)
7
>>> seed[1:len(sed)]

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    seed[1:len(sed)]
NameError: name 'sed' is not defined
>>> seed[1:len(seed)]
'104166'
>>> seed[1:len(seed)-1]
'10416'
>>> 
