#!/uer/bin/python
# -*- coding: UTF-8 -*-


"""
				@discrip: 斐波那契数列（Fibonacci sequence），又称黄金分割数列，
				                 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
					step1: initialize
					step2: 8in8out switch to usb
					step3: high voltage
					step4: 1in8out power from line8
					step5: connect to specific usb_port
				@line: the line number which is connected to device on 8in8out board
				@usb_port: the port on 1in8out connect to pc
 """

#from functools import lru_cache

#方法1
def fib(n):
	a,b = 0,1
	for i in xrange(n - 1):
		a,b = b,a+b
	return a

for i in xrange(1,11):
	print fib(i)

#方法2 使用递归
def fib2():
	if n == 1 or n == 2:
		return 1
	return fib(n - 1)+fib(n - 2)
print fib(10)
print"********"

#方法3 使用数学通式 #斐波那契数列通项公式#输出第n个数字
f = (1/(5 ** 0.5))*(((1+(5*0.5))/2)**i - ((1 - (5**0.5))/2)**i)
print"第%d个数:"%n,int(f)

#输出前n个数列
l = [1]
for i in xrange(1,n+1):
	f = (1/(5 ** 0.5))*(((1+(5*0.5))/2)**i - ((1 - (5**0.5))/2)**i)
	l.append(int(f))
print l
print"********"


#方法4 使用修饰器和缓存
#@lru_cache(None)
#def f(n):
#	assert n >= 0
#	return n if n<= 1 else f(n -1) + f(n - 2)
#print(f(10))
