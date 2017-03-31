#!/usr/bin/python
# -*- coding:UTF-8 -*-

tup1 = ('aa', 11, 'ss')
tup2 = (1,2,3,4,5)

print "tup1[0]:", tup1[0]
print "tup2[1:4]:", tup2[1:4]

tup3 = tup1 + tup2

print tup3
del tup3;
print "after deleting tup:"
print tup3