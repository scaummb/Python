#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        @discrip: 
                    step1:  import a backage
                    step2:  
                    step3: 
                    step4:  
                    step5:  
        @line:  
        @usb_port:  
        @company:Allwinner
        @author:mmb
 """

 #导入第三方库xlrd
import xlrd

def print_xls(path):    
	#path为.xls文件的保存路径              
	data = xlrd.open_workbook(path)   
	#sheet()方法打开excel的某个工作表
  	table = data.sheet()[0] 
  	#nrows获取sheet的行数          
   	nrows = table.nrows 

   	#遍历输出sheet的数据
   	for i in range(nrows):
    		ss = table.row_values(i)
    		for i in range(len(ss)):
    			print ss[i]
    		print'+++++++++++++++'

#文件调试入口
if _name_=='_main_':
	print_xls('D:\我的文档\桌面\Py+Excel')
