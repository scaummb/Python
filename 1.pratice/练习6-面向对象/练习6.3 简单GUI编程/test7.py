#!/usr/bin/python
# -*- coding: utf-8 -*-    

"""
				@discrip: a snake game
					step1: initialize
					step2: 8in8out switch to usb
					step3: high voltage
					step4: 1in8out power from line8
					step5: connect to specific usb_port
				@line: the line number which is connected to device on 8in8out board
				@usb_port: the port on 1in8out connect to pc
 """
# 导入 Tkinter 库
from Tkinter import *

class Bt_Init(object):
	"""docstring for BtInit"""
	def __init__(self, bt_Name):		
		self.bt_Name = bt_Name

	def processOk():
		print'OK button is clicked..'

          def processCancle():
	 	print'Cancle button is clicked..'

	def init_Bt():
		pass

	def bt_Pack():
	 	bt_Name.pack()	


class Li_Init(object):
	#内部静态变量
	li_string = []
	"""docstring for Li_Init"""
	def __init__(self, li_Name,string_input):		
		#构造器定义
		self.li_Name = li_Name
		self.ll = string_input
		
	def  li_Pack():
		#
		li_string.append(self.ll)
		for item in li :
			listb.insert(count,item)	
		#放置到主窗口中	
		self.li_Name.pack()			


class Win_init(object):
	"""docstring for Win_init"""
	def __init__(self, name):
		self.name = name

class String(object):
	"""docstring for String"""
	def __init__(self, arg):
		super(String, self).__init__()
		self.arg = arg
						

class Run(object):
	"""docstring for Run"""
	def __init__(self, arg):		
		self.arg = arg

class print(object):
	"""docstring for print"""
	def __init__(self, p_string):
		self.p_string = p_string
						

if __name__ == '__main__':
             root = Tk()
             bt_1 = Bt_Init(root)
             bt_2 = Bt_Init(root)
             list1 = Li_Init(root)
             list2 = Li_Init(root)	
             Run.mainloop()					