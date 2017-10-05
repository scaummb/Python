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

def processOk():
	print'OK button is clicked..'

def processCancle():
	print'Cancle button is clicked..'

# 创建窗口对象的背景色
root = Tk()   
window = Tk()

li = ['c','python','php','html','SQL','java']
movie = ['CSS','jQuery','Bootstrap']

#  创建两个列表组件
listb = Listbox(root)
listb2 = Listbox(root)

#创建两个按钮
btOk =Button(window,text = "OK",fg = "red",command = processOk)
btCancle = Button(window,text = "cancle",bg = "yellow",command = processCancle)

count,count2 = 0,0
for item in li :
	listb.insert(count,item)
	count += 1
for item2 in movie:
	listb2.insert(count2,item2)
	count2 += 1

# 将小部件放置到主窗口中
listb.pack()
listb2.pack()
btOk.pack()
btCancle.pack()

root.mainloop()
window.mainloop()







 
