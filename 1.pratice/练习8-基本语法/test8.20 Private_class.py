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

class JustCounter:
	"""docstring for JustCounter"""
	__secretCount = 0
	publicCount = 0

	def coount(self):
		#私有变量
		self.__secretCount += 1
		#公开变量
		self.publicCount += 1
		print self.__secretCount
	def count2(self):
		print self.__secretCount

counter = JustCounter()
#实例化后，调用含有私有类属性的函数时可以使用私有属性
counter.coount()
counter.coount()
counter.coount()
counter.coount()

print counter.publicCount

print counter._JustCounter__secretCount
#print counter.__secretCount
try :
	print counter.__secretCount
except AttributeError:
	print"JustCounter instance has no attribute '__secretCount'"
print"*****"
try:
	counter.count2()
except IOError as e:
	print"you can not use private attribute"
else:
	print "Ok"
finally:
	pass

