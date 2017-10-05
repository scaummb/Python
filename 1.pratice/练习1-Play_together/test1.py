# _*_ coding: utf-8 _*_
import os       
import test2	 #导入模块

test2.waitingok(3)      #调用模块的函数
print"Hello boys and girls,welcome to the pearl park.."
test2.waitingok(2)      
    
test2.waitingok(3)
while True:
  a = raw_input("I'm AlphaGo,tell me your name,please..\n")     #输入名字
  if(a != "0"):           
    print"hello,",a
    break
  else:
    print"tell me your name,please.."
    continue
test2.waitingok(2)

print"Here are some friends waiting for your coming.\n ....Let me show you who they are...."
test2.waitingok(2)
count = 1
FriendList = ['lili','xiaoming','dongdong','xiaohong']
for li in FriendList:  
  print'the',count,"friend's name is:",li
  count += 1
test2.waitingok(2)


while True:        
  answer = raw_input("Do you want to play with them?\n Y/N..\n")     
  if answer == 'Y' :       #Y,列表增加
    #print"Now we have ",(len(FriendList)+1),"little friends,and they're:/n"     
    count = 1
    FriendList.append(a)
    for li in FriendList:  
      print'the',count,'name is:',li
      count += 1            
    print'Now you are one of the group...'
    break
  elif answer == 'N':       #N,列表删除
    count = raw_input("Alright,we get next part,which one makes you unhappy?\n")
    count = int(count)             #类型转化
    del FriendList[count - 1]      #删除列表的一个元素
    for li in FriendList:  
      print'the',count,'name is:',li
      count += 1      
    print'Now you willnot see him anymore...'
    test2.waitingok(2)
    break
  else:                     #其他键入，则重新进行判断
    print'Please try again...'

             
while True:         #大循环
  answer1 = raw_input("Have a sum calculation game?\n Y/N..\n")    #是否进行加法运算
  if answer1 == 'Y':     #Y，进行下一步
    while True:
      b = raw_input("please input two numbers(<100) to make a sum..\n")
      b = int(b)
      if b >= 100:
        print'Your first input number is',b,',Please input another number below 100..\n'
        continue    
      c = raw_input("please input another..\n")
      c = int(c) 
      if c >= 100:
        print'Your second input number is',c,',Please input another number below 100..\n'
        continue              
      sum = test2.add(b,c)            
      print'The result is ',sum,'\n   Thanks..'
      break
    break
  elif answer1 == 'N':       #N,取消下一步
    print'Cancling.......'
    test2.waitingok(2)
    break
  else:                     #其他键入，则重新进行判断
    print'Please try again...'


