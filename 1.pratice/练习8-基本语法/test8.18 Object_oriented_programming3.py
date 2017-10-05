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

class Parent:
	parentAttr = 100
	"""docstring for Parent"""
	def __init__(self ):
		print"调用父类构造函数"

	def parentMethod(self):
		print"调用父类方法"

	def setAttr(self,attr):
		Parent.parentAttr = attr
		pass

	def getAttr(self):
		print"父类属性 :",Parent.parentAttr
		pass

class Child(Parent):
	"""docstring for Child"""
	def __init__(self):
		print"调用子类构造方法"

	def childMethod(self):
		print"调用子类方法 childMethon"

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
						
