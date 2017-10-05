# coding=utf-8

import sys
import os
from ViewModule.ViewModuleWiFi import ViewModuleWiFi

viewModuleWiFi = ViewModuleWiFi()

class OpenWiFi(object):
    """This case is aim to open wifi with view module wiwi interfaces
    @Discription: zhangzeliang@allwinnertech.com

    @Know issue: None

    @Todo: None
    """
    def __init__(self):
        print("Open WiFi")

    def open_wifi(self):
        '''This case is aim to open wifi
        @Description: zhangzeliang@allwinnertech.com
        @return: True or False
        '''
        if viewModuleWiFi.ae_open_wifi():
            print("Open WiFi successfully")
            return True
        else:
            assert False, "Fail to open WIFI"

demo = OpenWiFi()
demo.open_wifi()

