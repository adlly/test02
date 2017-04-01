#!/usr/bin/python
# -*- coding:UTF-8 -*-

def printinfo(arg1, *vartuple):
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return

printinfo(10);
printinfo(20,30,40)