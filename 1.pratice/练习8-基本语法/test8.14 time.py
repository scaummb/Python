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

import time

ticks = time.time()
print"Now is: ",ticks

local_time = time.localtime(time.time())
print"本地时间为 ：",local_time

print"**************"
print time.strftime("%y-%m-%d %H:%M:%S",time.localtime())

print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())

a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
