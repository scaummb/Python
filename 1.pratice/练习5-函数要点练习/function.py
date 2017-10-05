#!/usr/bin/python   python
# -*- coding: utf-8 -*-
'''
                          @discrip:this is a test case just for pratice
			step1:
			step2:
			step3;
		@company :Allwinner
		@author:moubinmo
'''
#导入operator模块的add、sub方法，以及random模块的randint,、choice方法
from operator import add, sub
from random import randint, choice

#创建一个字典，字符对应符号
action = {'+': add,'-': sub}
#试错机会
MAXTRIES = 2

def doprob():
	# choice函数，返回字符串序列的某一元素，加法或者减法
	op = choice('+-')
	# randint函数随机返回1--10之间的整数，[ ]内的for循环用法简化了代码量，nums为包含两个元素的序列
	nums = [randint(1,10) for i in range(2)]
	#sort是List类的一个方法，nums是List类的一个实例，reverse为True时，sort方法会对序列进行一个排序，元素值从大到小排列
	nums.sort(reverse = True)

	#这是较难理解的，action[op]是字典的一个value，根据前面op的key，将会决定value值，即add(*nums)或sub(*nums)，从而调用operator模块的add或者sub方法对nums列表的元素进行运算
	#同时结果保存在ans
	ans = action[op](*nums)

	#这个比较少见，赋值输出？？
	pr = '%d  %s  %d\n'%(nums[0],op,nums[1])
	oops = 0
	while True:
		#异常处理，判断结果与保存于ans的值是否一致
		try :
			if int(raw_input(pr)) == ans:
				print 'corrrect'
				break
			if oops == MAXTRIES:
				print'answer\n%s%d'%(pr, ans)
			else:
				print'incorrect...try again'
				oops += 1
		
		#异常输出
		except (KeyboardInterrupt,\
			 EOFError, ValueError) :
			print 'invalid input...try again'

def main():
	while True:
		doprob()
		try:
			opt = raw_input("Again?  [y]").lower()
			if opt and opt[0] == 'n':
				break
		
		#键值大小异常
		except (KeyboardInterrupt,EOFError):
			break

#__name__，一个内置变量，用于表示当前模块的名字，当前模块被直接运行时的模块名为__main__，运行以下的程序；相当于程序的模拟入口。
if __name__ == '__main__':
	main()		
