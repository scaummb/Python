#!/uer/bin/python
# -*- coding: UTF-8 -*-
"""
				@discrip: 运算符操作
					step1: initialize
					step2: 8in8out switch to usb
					step3: high voltage
					step4: 1in8out power from line8
					step5: connect to specific usb_port
				@line: the line number which is connected to device on 8in8out board
				@usb_port: the port on 1in8out connect to pc
 """

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

print "dic['Name']:",dict['Name']
print "dict['Age']:",dict['Age']
#print "dict['Alice']",dict['Alice']

dict['Age'] = 8
dict['School'] = "DSP School"

print"dict['Age']",dict['Age']
print"dict['School']",dict['School']

#dict.clear()
#print"dict['Age']",dict['Age']

dict['Age'] = 10000
print "dict['Age']",dict['Age']


print"************"
dictionary = {}
flag = 'a'
pape = 'a'
off = 'a'
while flag == 'a' or 'c':
    flag = raw_input("输入或查找？a/c")
    if flag == "a":
        word =  raw_input("输入Key:")
        defintion = raw_input("输入定义值value：")
        dictionary[str(word)] = str(defintion)
        print("添加成功")
        pape = raw_input("是否查字典？a/0")
        if pape == 'a':
              print dictionary
        else:
              continue
    elif flag == 'c':
        check_word = raw_input("要找哪个单词: ")
        for key in sorted(dictionary.key()):
              if str(check_word) == key:
                    print'存在',key,dictionary[key]
                    break
              else:
                    off = 'b'
        if off == 'b':
              print'sorry'
    else:
         print'error'
         break
        
