#!/usr/bin/python
# -*- coding: utf-8 -*-

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
 
def waitingok(a):    
    for a in range(1,a):    
        print'***********************'

def add(a,b):
    c = a + b
    return c
