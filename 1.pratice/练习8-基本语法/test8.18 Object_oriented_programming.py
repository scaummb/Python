#!/uer/bin/python
# -*- coding: UTF-8 -*-
"""
				@discrip: 
					step1: initialize
					step2: 8in8out switch to usb
					step3: high voltage
					step4: 1in8out power from line8
					step5: connect to specific usb_port
				@line: the line number which is connected to device on 8in8out board
				@usb_port: the port on 1in8out connect to pc

 """
class Employee(object):
	"""所有员工的基类"""
	#empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。\
	#你可以在内部类或外部类使用 Employee.empCount 访问。
	empCount = 0

	#构造函数，创造了函数就会调用这个方法
	def __init__(self, name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def dispalyCount(self ):
		print"Total Employee  %d" % Employee.empCount

	def displayEmployee(self):
		print"name :",self.name,",Salary: ",self.salary
		
class Test:
	"""docstring for test"""
	def prt(self):
		print(self)
		print(self.__class__)

emp1 = Employee("mmb",20000)
emp2 = Employee("hhq",900000)
t = Test()

t.prt()
emp2.displayEmployee()
emp1.displayEmployee()
print "Total Employee %d"% Employee.empCount
print"***"		

emp1.age = 7
emp2.age = 10s
del emp1.age

getattr(emp1,'age')
hasattr(emp1,'age')
setattr(emp1,'age',8)
delattr(emp1,'age')
print"***"	

print"Employee.__doc__:",Employee.__doc__
print"Employee.__name__:",Employee.__name__
print"Employee.__modue__:",Employee.__modue__
print"Employee.__based__:",Employee.__based__
print"Employee.__doc__:",Employee.__dict__
print"***"	

