#/usr/bin/python
# -*- coding: UTF-8 -*-


# 列表用[]表示
# '+'表示连接,'*'表示重复

list = ['aaa', 456,65.25,'dks',25.01]
tinylist = ['dfd',4556]

print list
print list[0]
print list[1:3]
print list[2:]
print tinylist * 2
print list+tinylist


#元组用()表示,元组不可二次赋值,相当于只读列表

tuple = ('runoob',456,2.23,'john',213.454)
tinytuple = ('1sdfs',15431)

print tuple
print tuple[0]
print tuple[1:3]
print tuple[2:]
print tinytuple*2
print tuple+tinytuple

#字典 {}表示  列表时有序的对象集合,字典是无序的对象集合

dict = {}
dict['one'] = "this is a shit"
dict[2] = "this is an another shit"
tinydict = {'name':'join','code':4572,'dept':'sdfs'}

print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()