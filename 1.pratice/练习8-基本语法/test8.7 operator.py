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

print"*******calculation********"

a = 21
b = 10
c = 0

c = a + b
print"1 - c = ",c

c = a - b
print"2 - c = ",c

c = a * b
print"3 - c = ",c

c = a/b
print"4 - c =",c

c = a % b
print"5 - c = ",c

a = 2
b = 3
c = a * b
print"6 - c = ",c

a = 10
b = 5
c = a//b
print"7 - c = ",c

print"*******compare********"

a = 21
b = 10
c = 0

if (a == b):
    print"1 a== b"
else:
    print"2 a != b"
if (a != b):
    print"3 a!= b"
else:
    print"4 a == b"
if (a > b):
    print"5 a > b"
else :
    print"6 a < b"
if(a > b):
    print"7 a > 6"
else:
    print"8 a < b"


a = 5
b = 20
if (a <= b):
    print"a <= b"
else:
    print"a > b"

if(b >= a):
    print"a >= b"
else:
    print"a < b"

print"*******giving_value*******"

a = 21
b = 10
c = 0

c = a + b
print"1 c:",c

c += a
print"2 c:",c

c *= a
print"3 c:",c

c /= a
print"4 c:",c

c = 2
c %= a
print"5 c:",c

c **= a
print"6 c:",c

c //= a
print"7 c:",c


print"*******bit_operator********"
#60=0011 1100
#13=0000 1101
a = 60
b = 13
c = 0

c = a & b
print"1 c",c

c = a | b
print"2 c",c

c = a ^ b
print"3 c",c

c = ~a
print"4 c",c

c = a << 2
print"5 c",c

c = a >> 2
print"6 c",c


print"*******Logical_operator********"
a = 10
b = 20

if(a and b):
    print"1 True"
else:
    print"2 one is not true"
if(a or b):
    print"3 True"
else:
    print"4 all are not true"

a = 0
if (a and b):
    print"5 true"
else:
    print"6 one is not true.."

if(a or b):
    print"7 True"
else:
    print"8 all are not true"

if not(a and b):
    print"9 false"

else:
    print"10 all true"

    
print"*******menber_operator********"
a = 10
b = 20
list = [1,2,3,4,5]

if(a in list):
    print"1 yes"
else:
    print"2 No"

if(b not in list):
    print"3 No"
else:
    print"4 yes"

a = 2
if(a in list):
    print"5 yes"
else :
    print"6 No"


print"*******identification_operator********"
a = 20
b = 20

if (a is b):
    print"1 same"
else:
    print"2 dif"
if (a is not b):
    print"3 dif"
else:
    print"4 same"

b = 30
if(a is not b):
    print"5 dif"
else:
    print"6 same"
if(a is b):
    print"7 same"
else:
    print"8 dif"


print"*******priolity_of_operator********"
a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b)*c/d
print e

e = ((a + b)* c)/d
print e

e = (a + b)*(c/d)
print e

e = a + (b*c)/d
print e



print"*******9*9multiplication_table********"
for i in range(1,9):
    print
    for j in range(1,i+1):
        print"%d*%d = %d"%(i,j,i*j)

        



