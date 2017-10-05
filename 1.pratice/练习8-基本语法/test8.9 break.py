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
for letter in 'Python':
    if letter == 'h':
        break
    print'当前：',letter

var = 10

while var > 0:
    print '当期变量值:',var
    var -= 1
    if var == 5:
        break
print"Goodbye"
print"***************"
for letter in 'Python':
    if letter == 'h':
        continue
    print'当前：',letter

var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print'当期变量值:',var
print"Goodbye"
