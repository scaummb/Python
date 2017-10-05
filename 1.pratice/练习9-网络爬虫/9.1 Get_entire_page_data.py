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
import urllib

def GetHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

html = GetHtml("http://www.mmjpg.com/")

print html