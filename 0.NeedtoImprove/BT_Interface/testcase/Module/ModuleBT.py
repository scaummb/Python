#!/usr/bin/python
# -*- coding: UTF-8 -*-

from UIProperty import UiProperty
from TestData import TestData
from uiautomator import Device

UiProperty = UiProperty()
TestData = TestData("SETTING")

class ModuleBT():
    """About BlueTooth module operation with wifi interfaces

        @Discription: moubinmo@allwinnertech.com

        @know issue: None

        @Todo: Done
    """
    def __init__(self):
        # Initialize const number
        self._TIME_OUT = 2000
        self._DELAY_TIME = 2
        self._CLICK_LOOP_TIME = 5
        # Initialize UI Property and Test Data
        self.__init_module_ui_property()
        self.__init_module_test_data()
        # Create device object
        self._device = Device(self._td_device_serial)

    def __init_module_test_data(self):
        """Get module test data"""
        self._td_device_serial = TestData.get_str()


class ModuleWifi():
    """About wifi module operation with wifi interfaces

        @Discription: zhangzeliang@allwinnertech.com

        @Know issue: None

        @Todo: None
        """
    def __init__(self):
        # Initialize const number
        self._TIME_OUT = 2000
        self._DELAY_TIME = 2
        self._CLICK_LOOP_TIME = 5
        # Initialize UI Property and Test Data
        self.__init_module_ui_property()
        self.__init_module_test_data()
        # Create device object
        self._device = Device(self._td_device_serial)

    def __init_module_test_data(self):
        """Get  module test data"""
        self._td_device_serial = TestData.get_str("Device", "serial", "common")

    def __init_module_ui_property(self):
        """Get  module ui test data
        """
        self._uip_wifi = UiProperty.GetUIProperty("WiFi")
        self._uip_wifi_switch_widget = UiProperty.GetUIProperty("WiFiSwitchWidget")

    def switch_wifi(self,OnOff):
        """Click and switch wifi in advanced settings interface
        @Discription: zhangzeliang@allwinnertech.com
        @Para OnOff: 打开、关闭
        @Return:True or False
        """
        print ("Start to excute SwitchWiFi")
        if self._device(**self._uip_wifi).wait.exists(timeout=self._TIME_OUT):
            print ("Find WiFi successfully")
            for i in range(self._CLICK_LOOP_TIME):
                if self._device(**self._uip_wifi).right(**self._uip_wifi_switch_widget):
                    WiFiStatus = self._device(**self._uip_wifi).right(**self._uip_wifi_switch_widget).get_text()
                    if WiFiStatus == OnOff:
                        print ("WiFi status is %s currently"%OnOff)
                        return True
                    else:
                        print ("WiFi status is not %s currently, now click and switch status" % OnOff)
                        self._device(**self._uip_wifi).click()
                        i += 1
                else:
                    print("Not find WiFi Switch Widget")
                    return False
            else:
                print("Fail to switch WiFi status")
                return False
        else:
            print ("Not find WiFi")
            return False





