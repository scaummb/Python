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

d = []

for i in xrange(1,5):
	for j in xrange(1,5):
		for k in xrange(1,5):
			if(i != k) and (i != j) and (j != k):
				#print i,j,k
				d.append([i,j,k])
print"总数量：",len(d)
print d








