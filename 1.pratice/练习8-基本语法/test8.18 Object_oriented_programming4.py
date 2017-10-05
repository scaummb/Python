#!/uer/bin/python
# -*- coding: UTF-8 -*-
"""
				@discrip: 
					step1: initialize
					step2: 8in8out switch to usb
					step3: high voltage
					step4: 1in8out power from line8
					step5: connect to specific usb_port
				@line: the line number which is connected to device on 8in8out board
				@usb_port: the port on 1in8out connect to pc

 """

class Parent(object):
	"""docstring for Parent"""
	def myMethod(self):
		print"a 调用父类方法"

class Child(Parent):
	"""docstring for Child"""
	def myMethod(self):
		print"b 调用子类方法"

c = Child()
c.myMethod()
		
		
		

