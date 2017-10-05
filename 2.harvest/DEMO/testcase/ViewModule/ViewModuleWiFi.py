#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import sys
import os
from sys import path
sys.path.append("../")
from Module.ModuleWifi import ModuleWifi
from Module.ModuleSetting import ModuleSetting
from Module.TestData import TestData
from uiautomator import Device

GetTestData = TestData("WIFI")
ModuleSetting = ModuleSetting()
ModuleWifi = ModuleWifi()

class ViewModuleWiFi(object):
    """About setting module operation with module setting interfaces

    @Discription: zhangzeliang@allwinnertech.com

    @Know issue: None

    @Todo: None
    """

    def __init__(self):
        # initialize for module UI property and  module test data
        self.init_module_test_data()
        # Create device object
        self._device = Device(self._td_device_serial)

    def init_module_test_data(self):
        """Get  module test data"""
        self._td_device_serial = GetTestData.get_str("Device", "serial", "common")

    # This interface of OpenWiFi is to open wifi
    def ae_open_wifi(self):
        """open wifi via call module interface in class of ModuleSetting and ModuleWifi
        @return: True or False
        """
        print ("Start excute open_wifi")
        if ModuleSetting.select_settings():
            if ModuleSetting.enter_common_settings():
                if ModuleSetting.enter_advanced_setting():
                    if ModuleWifi.switch_wifi(u"打开"):
                        print ("Open wifi successfully")
                        return True
                    else:
                        assert False,"Fail to switch wifi"
                else:
                    assert False,"Fail to enter advanced Setting"
            else:
                assert False,"Fail to enter common setting"
        else:
            assert False,"Fail to select settings"






