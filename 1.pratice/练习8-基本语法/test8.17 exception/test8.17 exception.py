#!/uer/bin/python
# -*- coding: UTF-8 -*-
"""
				@discrip: 异常
					step1: initialize
					step2: 8in8out switch to usb
					step3: high voltage
					step4: 1in8out power from line8
					step5: connect to specific usb_port
				@line: the line number which is connected to device on 8in8out board
				@usb_port: the port on 1in8out connect to pc

 """

import sys
sys.path.append("D:\我的文档\桌面\练习\练习8-基本语法\test8.17 exception")

class Networkerror(RuntimeError):
    def __init__(self,arg):
        self.args = arg        

def temp_convert(ver):
    try:
        return int(ver)
    except ValueError,Argument:
        print"arg has no number...",Argument

def functinonname(level):
    if(level < 1):
        raise Exception("Invalid level!",level)
    else:
        print"*"
#chmod -w test.txt 

try:
    fh = open("test","w")
    fh.write("It's a test file")
except IOError:
    print"Error:no file"
else:
    print"write sucessfully"
    fh.close()



try:
    fh = open("test","w")
    fh.write("test file is for testing")
finally:
    print"No such file.."

try:
    fh = open("test","w")
    try:
        fh.write("test exception")
    finally:
        print"close"
        fh.close()
except:
    print"Error"

temp_convert("xyz")
print"*******"

try:
    functinonname(0)
except "Invalid level!":
    print 1
else:
    print 2
finally:
    print"*"
    
try:
    raise Networkerror("Bad hostname")
except Networkerror,e:
    print e.args
