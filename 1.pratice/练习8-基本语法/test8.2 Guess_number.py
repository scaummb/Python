#!/uer/bin/python
# -*- coding: UTF-8 -*-
"""
		@discrip: 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
			step1: x + 100 = n2, x + 100 + 168 = m2
			step2: 计算等式：m2 - n2 = (m + n)(m - n) = 168
			step3: 设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
			step4: m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
			step5: 从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
			step6: 由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
		@line: the line number which is connected to device on 8in8out board
		@usb_port: the port on 1in8out connect to pc
 """

for i in range(1,85):
    #逆推的第一个条件：i 能整除 168
    if 168 % i == 0:
        #同理，j 等于 168/i
        j = 168 / i
        #i>j一次遍历
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n -100
            print (x)

