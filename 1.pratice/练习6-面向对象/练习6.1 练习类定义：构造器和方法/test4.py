#!/usr/bin/python
# -*- coding: utf-8 -*-

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
class MyDataWithMethod(object):
	"""docstring for ClassName"""
	def __init__(self, arg):		
		self.arg = arg
		print'You are',arg
	def printFoo(self):
		print 'You are the best guy  today among the past life...'

if __name__ == '__main__':
	mmb = 'MMB'
	happyGuy = MyDataWithMethod(mmb)
	happyGuy.printFoo()













