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
l = []
li = [1,5,4,6,3,8]

n = len(li) 

#第0中方法
while 1:
	try:
		for i  in xrange(3):
			    x = int(raw_input("integer:\n"))
			    l.append(x)
		print(sorted(l))
		break
	except Exception as e:
		print"Please Input an intrger."
	


#第一种方法
l.sort()
print l
print'逆序'
l.sort(reverse=True)
print l


#第二种方法，字典的方法
a = {"x":l[0],"y":l[1],"z":l[2]}
print"**********"
for w in sorted(a,key=a.get):
	print w,a[w]

#第三种方法
print"**********"
for i in xrange(0,n):
	for j in xrange(i,n):
		if (li[i] >= li[j]):
			tmp = li[i]
			li[i] = li[j]
			li[j] = tmp
print li

#第四种方法
print"**********"
k1 = l[0]
k2 = l[1]
Max = max(k1,k2)
Min = min(k1,k2)
if l[2] > Max:
	print l[2],Max,Min
elif l[2] < Min:
	print Max,Min,l[2]
else:
	print Max,l[2],Min

#第五种方法
arr = l
for m in xrange(0,3):
	for mm in xrange(0,3):
		for mmm in xrange(0,3):
			if arr[m] > arr[mm] >arr[mmm]:
				print arr[m] ,arr[mm] ,arr[mmm]
