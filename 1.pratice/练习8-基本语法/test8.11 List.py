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

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

list01 = ['runoob', 786, 2.23, 'john', 70.2]
list02 = [123, 'john']

print"list1[0]:",list1[0]
print"list2[1:5]",list2[1:5]


print "Value available at index 2 : "
print list1[2];
list1[2] = 2001;
print "New value available at index 2 : "
print list1[2];

print list1
del list1[2]
print"After deleting:"
print list1

print"**********************"

print list01
print list02

print list01[0]
print list01[-1]
print list01[0:3]

print list01 * 2

print list01 + list02

print len(list01)

del list02[0]
print list02

print 'join' in list02

for i in list01:
    print i

print cmp(list01,list02)

print max([0,1,2,3,4])
print min([0,1])

atuple = (1,2,3,4)
list03 = list(atuple)
print list03

list03.append(5)
print list03

list03.extend(list01)
print list03

print list03.count(1)

print list03.index('john')

list03.insert(0,'hello')
print list03

list03.remove(1)
print list03

list03.reverse()
print list03

list03.sort()
print list03
