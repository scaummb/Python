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
#导入库
import os
import string
import String2                     

#字符串合并赋值
alphas = string.letters + ' '      
nums = string.digits               

print alphas
print nums  
#声明密码列表
passwords = []		

String2.waitingok(2)
while True :
	myPassword = raw_input('Please input your own ID card password,each word should be selected in the alphabet and the number table:')    
	q = len(myPassword)  
		#检查密码是否有误
	if q < 6:
		print'Please input a password longer than 6 bits'
		continue
	elif myPassword[0] not in alphas:
		print"Invalid!!The first symble must be alphabetic"  #首字符必须是字符
		continue
	else:
		for otherChar in myPassword[1:]:
			if otherChar not in alphas + nums:				 #检查其余字符
				print"Invalid:remaining must be alphanumeric.."
				break

		break
passwords.append(myPassword)   #转化为列表  	
String2.waitingok(1)

while True:           
    a = raw_input("Do you want to change your ID card passcode?    Y/N   \n")               #是否改变设定的密码
	if a == 'Y' :       #Y,列表增加
		b = raw_input("Which one do you want to replace? ")			#列表的具体某一位代替 
		b = int(b) 				                                    #类型转换
		print'b = %d'%b
		String2.waitingok(2)
		c = raw_input("Which alpha or number do you want to replace with ? ")		#输入新值替代旧值
		myPassword2 = myPassword[:b] + c + myPassword[b+1:]
		print'your ID card passcode now is :',myPassword2
		String2.waitingok(2)
		break
	elif a == 'N':         
		print'Your ID card password is :',passwords
		String2.waitingok(2)
		break
	else:                      
		print'Please try again...'

String2.waitingok(3)

count = 1
notebook = {'Bank':11,'Home':22,'Schoo':33}
while True:
	d = raw_input("You have lots of passcodes in the notebook,would you want to search them?   Y/N  ")    #密码本的显示
	if d == 'Y':
		#count = 1
		for key in notebook:			#±éÀú×Öµä
			print'NO.%d    key = %s,value = %s \n'%(count,key,notebook[key])  	  
			count += 1
		print'That is all..'
		break
	elif d == 'N':
		print'Ok............'
		break
	else:
		print'Please try again...'
String2.waitingok(2) 


while True:
	e = raw_input("Do you want to add the ID card item into the notebook?    Y/N \n")            #是否添加密码进密码本
	count = 1
	if e == 'Y':
		#count = 1
		notebook['ID card'] = passwords
		for key in notebook:			 
			print'NO.%d    key = %s,value = %s \n'%(count,key,notebook[key])        # 输出合并后的密码本
			count += 1
		print'That is all..'
		break 
	elif d == 'N':
		for key in notebook:			 
			print'NO.%d    key = %s,value = %s \n'%(count,key,notebook[key])  	    # 输出不合并的密码本
			count += 1
		print'That is all..'
		break
	else:
		print'Please try again...\n'
String2.waitingok(2) 
print'exiting............\n'

