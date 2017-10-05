#!/uer/bin/python
# -*- coding: UTF-8 -*-
"""
				@discrip: 运算符操作
					step1: initialize
					step2: 8in8out switch to usb
					step3: high voltage
					step4: 1in8out power from line8
					step5: connect to specific usb_port
				@line: the line number which is connected to device on 8in8out board
				@usb_port: the port on 1in8out connect to pc
 """

def ChangeInt (a):
    a = 10
def changeme(mylist):
    mylist.append([1,2,3,4])
    print "inside:",mylist
    return
def printinfo(name,age):
    print"name = ",name
    print"age = ",age
    return
def printfo2(name,age = 35):
    print"name:",name
    print"age:",age
    return
def printinfo2(arg1,*vartuple):
    print arg1
    for var in vartuple:
        print"*"
        print var
    return
def sum2 (arg1,arg2):
    total = arg1 + arg2
    print "inside:",total
    return total
def sum3 (arg1,arg2):
    global total3
    total3 = arg1 + arg2
    print "inside:",total3
    return total3


b = 2
mylist = [10,20,3,0]
total = 0
total3 = 0

ChangeInt(b)
print b
changeme(mylist)
print "outside:",mylist
changeme(mylist = [000,0,0,0,0])
print "outside:",mylist
printinfo(age = 10,name = 'mmb')
print"**********"
printfo2(age = 49,name = 'mmbb')
print"** **"
printfo2(name = 'mb')
print"** **"
printinfo2(109)
printinfo2(45648,2152,55)

print"** 匿名函数 **"
sum = lambda arg1,arg2:arg1 + arg2
print"result is :",sum(45646,45654)

print"** 作用域 **"
sum2(12,45)
print "outsiade；",total
sum3(1,1)
print "outsiade；",total3



