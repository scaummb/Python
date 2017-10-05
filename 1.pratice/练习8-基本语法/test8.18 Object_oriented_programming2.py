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

 class Point(object):
 	"""docstring for Point"""
 	def __init__(self,x,y):
 		self.x = x
 		self.y = y
 	def __del__(self):
 		class_name = self.__class__.__name__
 		print class_name,"销毁"
 pt1 = Point()
 pt2 = pt1
 pt3 = pt1
 print id(pt1),id(pt2),id(pt3)
 del pt1
 del pt2
 del pt1