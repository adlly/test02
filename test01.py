#!/usr/bin/python
# -*- coding:UTF-8 -*-

list01 = ['runoob', 786, 2.23, 'john', 70.2]
list02 = [123, 'john']
print list01
print list02

print list01[0]
print list02[-1]
print list01[0:3]

print list01 * 2

print list01 + list02

print len(list01)

del list02[0]
print list02

print 'john' in list02

for i in list01:
    print i

print cmp(list01,list02)

print max([0,1,2,3,4])

print min([0,1])

aTuple = (1,2,3,4)
list03 = list(aTuple)
print list03

list03.append(5)
print list03

list03.extend(list01)
print list03

print list03.count(1)

print list03.index('john')

list03.insert(0,'hello')
print list03

print list03.pop(0)
print list03

list03.remove(1)
print list03

list03.reverse()
print list03

list03.sort()
print list03