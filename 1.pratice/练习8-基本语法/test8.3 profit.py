#!/uer/bin/python
# -*- coding: UTF-8 -*-
"""
				@discrip: switch device to slave usb
					step1: initialize
					step2: 8in8out switch to usb
					step3: high voltage
					step4: 1in8out power from line8
					step5: connect to specific usb_port
				@line: the line number which is connected to device on 8in8out board
				@usb_port: the port on 1in8out connect to pc
 """

i = int(raw_input("净利润："))
#!利润值分界点：列表数据
arrr = [1000000,600000,400000,200000,100000,0]
#!提成利率
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
#!利润总和
r = 0
#!比较边界值顺序由大至小更加方便
for idx i range (0,6):
    if i  > arr[idx]:
        r += (i - arr[idx])*rat[idx]
        print (i - arr[idx])*rat[idx]
        i =arr[idx]
print r
