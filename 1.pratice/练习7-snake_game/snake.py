#!/usr/bin/python
# -*- coding: utf-8 -*-    

"""
                @discrip: a snake game
                    step1: initialize
                    step2: 8in8out switch to usb
                    step3: high voltage
                    step4: 1in8out power from line8
                    step5: connect to specific usb_port
                @line: the line number which is connected to device on 8in8out board
                @usb_port: the port on 1in8out connect to pc
 """

from Tkinter import *
import tkMessageBox,sys
from random import randint
 

 #坐标类，它的属性方法是获取坐标和显示坐标
class Grid(object):
    #隐式调用
    def __init__(self,master=None,window_width=800,window_height=600,grid_width=50,offset=10):
        #Grid类的属性有：master、window_width、window_height、grid_width、offset
        self.height = window_height
        self.width = window_width
        self.grid_width = grid_width
        self.offset = offset
        self.grid_x = self.width/self.grid_width
        self.grid_y = self.height/self.grid_width
        self.bg = "#EBEBEB"
        self.canvas = Canvas(master, width=self.width+2*self.offset, height=self.height+2*self.offset, bg=self.bg)
        self.canvas.pack()
        self.grid_list()

    #作图方法
    def draw(self, pos, color,):
        x = pos[0]*self.grid_width + self.offset
        y = pos[1]*self.grid_width + self.offset
        self.canvas.create_rectangle(x, y, x+self.grid_width, y+self.grid_width,fill=color,outline=self.bg)
   
    # grid()方法得到当前的
    def grid_list(self):
        grid_list = []
        for y in range(0,self.grid_y):
            for x in range(0,self.grid_x):
                grid_list.append((x,y))
        self.grid_list = grid_list
    def __init__(self, Grid):
        #食物属性赋值，Grid为传入的参数
        self.grid = Grid


 #食物类，属性是坐标和画图
class Food(object):
        self.color = "#23D978"        
        self.set_pos()
    
    #随机产生食物的坐标
    def set_pos(self):
        x = randint(0,self.grid.grid_x - 1)
        y = randint(0,self.grid.grid_y - 1)
        self.pos =  (x, y)    
    #展示图片
    def display(self):
        self.grid.draw(self.pos,self.color)
 

 #蛇类，属性方法是改变转向，显示
class Snake(object):
    def __init__(self, Grid):
        self.grid = Grid
        self.body = [(10,6),(10,7),(10,8)]
        self.direction = "Up"
        self.status = ['run','stop']
        self.speed = 300
        self.color = "#5FA8D9"        
        self.food = Food(self.grid)
        self.display_food()
        self.gameover = False
        self.score = 0
    def available_grid(self):
        return [i for i in self.grid.grid_list if i not in self.body[2:]]
    def change_direction(self, direction):
        self.direction = direction
    def display(self):
        for (x,y) in self.body:
            self.grid.draw((x,y),self.color)
    def display_food(self):
        while(self.food.pos in self.body):
            self.food.set_pos()
        self.food.display()
    def move(self):
        head = self.body[0]
        if self.direction == 'Up':
            new = (head[0], head[1]-1)
        elif self.direction == 'Down':
            new = (head[0], head[1]+1)
        elif self.direction == 'Left':
            new = (head[0]-1,head[1])
        else:
            new = (head[0]+1,head[1])
        if not self.food.pos == head:         
            pop = self.body.pop()
            self.grid.draw(pop,self.grid.bg)
        else:
            self.display_food()
            self.score += 1
        self.body.insert(0,new)      
        if not new in self.available_grid():
            self.status.reverse()            
            self.gameover = True
        else:
            self.grid.draw(new,color=self.color)
 
 #游戏类，作为一个游戏，它具备了两个功能：启动游戏和根据键盘做出反应
class SnakeGame(Frame):
    #构造器定义
    def __init__(self,master=None, *args, **kwargs):

        #创建了子类Frame，它继承了Tk父类的属性，同时在__init__设置了一个新的实例属性master
        Frame.__init__(self, master)
        #子类Frame的变量master值为None
        self.master = master
        #SnakeGame的grid为Grid的一个实例，snake为Snake的实例，
        self.grid = Grid(master=master,*args, **kwargs)  
        self.snake = Snake(self.grid)
        self.bind_all("<KeyRelease>", self.key_release)
        self.snake.display()
    #启动方法
    def run(self):
        if not self.snake.status[0] == 'stop':
            self.snake.move()
        if self.snake.gameover == True:
            message =  tkMessageBox.showinfo("Game Over", "your score: %d" % self.snake.score)
            if message == 'ok':
                sys.exit()
        self.after(self.snake.speed,self.run)
    #获取键盘值方法
    def key_release(self, event):
        key = event.keysym
        key_dict = {"Up":"Down","Down":"Up","Left":"Right","Right":"Left"}
        if key_dict.has_key(key) and not key == key_dict[self.snake.direction]:
            self.snake.change_direction(key)
            self.snake.move()
        elif key == 'p':
            self.snake.status.reverse()
 

if __name__ == '__main__':
    #新创建一个窗口类的实例root
    root = Tk()
    snakegame = SnakeGame(root)
    snakegame.run()
    #mainloop()方法，监测SnakeGame对象有事件发生，就刷新组件
    snakegame.mainloop()


    