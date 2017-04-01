#!/usr/bin/python
# -*- coding:UTF-8 -*-

def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print b


def changeme(mylist2):
    mylist2.append([1,2,3,4])
    print "函数内取值:",mylist2
    return

mylist = [10,20,30]
changeme(mylist)
print "函数外取值:",mylist
