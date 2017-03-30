#!/usr/bin/python
# -*- coding:UTF-8 -*-

for letters in 'Python':
    if letters == 'h':
        continue
    print '当前字母: ' + letters

var = 10
while var > 0:
    var = var - 1
    if(var == 5):
        continue
    print '当前变量值: ' , var
print "Good bye!"
