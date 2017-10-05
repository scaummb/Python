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

import os
import divide

#定义类
class AddrBookEntry(object):
	"""docstring for AddrBookEntry"""
	def __init__(self, nm,py):
		'sfe version for __init__'
		#异常处理，防止构造器传参数出错
		try:
		self.name = nm
		self.phone = py
		print'Created instance for: %s,and your number is %d \n'%(self.name,self.phone)
		
		#如果参数错误，执行反馈
		except Exception as e:
			print'Something wrong......\n',e
	def updatePhone(self,newph):
		self.phone = newph
		print 'Now your phone number has been changed for : ',self.name

#main()函数
def  main ():
	a = [5,6]	
	#创建两个实例MyFirstClass与MySecondClass
	MyFirstClass = AddrBookEntry(a[0],18819467607)
	divide.waitingok(2)
	MySecondClass = AddrBookEntry(a[1],12345678955)
	divide.waitingok(2)
	while True:
		a = raw_input("Who are you?\n")	
		if a == '5':
			print'I konw your number:',MyFirstClass.phone
			break
		elif a == '6':
			print'I konw your number:',MySecondClass.phone
			break
		else:
			print'Please try again..'

	print'+++++++++++++++'
	while  True:
		b = raw_input("We will build a new class,\
			now please input your name.....\n")
		c = raw_input("Now please input your phone number..\n")
		try :
			MyThirdClass = AddrBookEntry(a,b)
			print'I konw your number:',MyFirstClass.phone
			print'I konw your number:',MySecondClass.phone			
		except ValueError as f:
			print'Please try again..'
		else:
			print'Thanks ,goodbye..'
			break


if __name__ == '__main__':
	main()
		
		












