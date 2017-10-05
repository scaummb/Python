#!/uer/bin/python
# -*- coding: UTF-8 -*-
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
import time
import sys

def isLeapYear(a):
    if(a%4 == 0 or a %400 == 0) and a %100 != 0 :
        return 1
    else:
        return 0

dict = {1: 31, 2: 28, 3: 31,4: 30, 5: 31, 6: 30, 7: 31, \
         8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

m = 0
        
year = int (raw_input("year: \n"))
month = int (raw_input("month: \n"))
day = int (raw_input("day: \n"))
#闰年
months1 = [0,31,60,91,121,152,182,213,244,274,305,335,366] 
#平年
months2 = [0,31,59,90,120,151,181,212,243,273,304,334,365]
#闰年
months11 = [31,29,31,30,31,30,31,31,30,31,30,31]  
#平年
months22 = [31,28,31,30,31,30,31,31,30,31,30,31]

#第一种方法
if ((year%4 == 0)and (year%100 != 0)) or ((year %100 == 0)and(year %400 ==0)):
    Dth = months1[month - 1]+day
else:
    Dth = months2[month - 1]+day
print"这是该年的第%d天"%Dth


#第二种方法 
if year % 100 == 0:
    if year % 400 == 0:
        days = sum(months11[0:month-1]) + day
    else:
        days = sum(months22[0:month-1]) + day
else:
    if year % 4 == 0:
        days = sum(months11[0:month-1]) + day
    else:
        days = sum(months22[0:month-1]) + day

print"%d.%d.%d是%d年的第%d天。"%(year,month,day,year,days)


#第三种方法
for i in range(1,month):
        m = m + dict[i]
m = m + isLeapYear(year) + day
print m 


#第四种方法
#reload(sys)
#sys.setdefaultencoding('utf-8')
a = raw_input("输入时间:格式2022-2-22：")
t = time.strptime(a,"%Y-%m-%d")
print'******'
print time.strftime("今年的第%j",t).decode('utf-8')
