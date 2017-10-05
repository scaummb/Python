#!/usr/bin/python
# -*- coding: UTF-8 -*-

from uiautomator import Device
from UIProperty import UiProperty
from TestData import TestData

UiProperty = UiProperty()
TestData = TestData("SETTINGS")

class ModuleSetting():
    """About setting module operation with setting interfaces

    @Discription: zhangzeliang@allwinnertech.com

    @Know issue: None

    @Todo: None
    """

    def __init__(self):
        # Initialize const number
        self._TIME_OUT = 2000
        self._DELAY_TIME = 2
        self._RETURN_BACK_LOOP_TIME = 20
        self._CLICK_LOOP_TIME = 5
        # Initialize UI Property and Test Data
        self.__init_module_ui_property()
        self.__init_module_test_data()
        # Create device object
        self._device = Device(self._td_device_serial)


    def __init_module_test_data(self):
        """Get  module test data"""
        self._td_device_serial = TestData.get_str("Device", "serial", "TestData")

    def __init_module_ui_property(self):
        """Get  module ui test data
        @Discription: zhangzeliang@allwinnertech.com
        # Modify self._uip_settings name
        # Add self._uip_common_setting_list
        """
        self._uip_settings = UiProperty.GetUIProperty("Settings")
        self._uip_common_settings = UiProperty.GetUIProperty("CommonSettings")
        self._uip_advanced_settings = UiProperty.GetUIProperty("AdvancedSettings")
        self._uip_common_setting_list = UiProperty.GetUIProperty("CommonSettingList")
        self._uip_action_bar_title = UiProperty.GetUIProperty("ActionBarTitle")

    def select_settings(self):
        """Click and select setting module at home interface
        @Return:True or False
        """
        print("Start to excute SelectSettings")
        for i in range(self._RETURN_BACK_LOOP_TIME):
            if self._device(**self._uip_settings).wait.exists(timeout=self._TIME_OUT):
                print ("Find Settings successfully")
                self._device(**self._uip_settings).click()
                if self._device(**self._uip_settings).isSelected():
                    print ("Select Settings successfully")
                    return True
                else:
                    print ("Fail to select Settings")
            self._device.press.home()
            self._device.press.back()
            i+=1
        else:
            print ("Fail to find Settings")
            return False

    def enter_common_settings(self):
        """Click and enter common setting module at home interface
        @Return:True or False
        """
        print("Start to excute EnterCommaonSettings")
        if self._device(**self._uip_common_settings).wait.exists(timeout=self._TIME_OUT):
            print ("Find Common Settings successfully")
            for i in range(self._CLICK_LOOP_TIME):
                if self._device(**self._uip_common_settings).isFocused():
                    print ("Select Common Settings successfully")
                    print "sself._uip_common_setting_list:", self._uip_common_setting_list
                    for j in range(self._CLICK_LOOP_TIME):
                        if self._device(**self._uip_common_setting_list).wait.exists(timeout=self._TIME_OUT):
                            print ("Enter into Common Settings successfully")
                            return True
                        else:
                            self._device(**self._uip_common_settings).click()
                            j += 1
                            self._device.delay(self._DELAY_TIME)
                            print "j:",j
                else:
                    self._device(**self._uip_common_settings).click()
                    self._device.delay(self._DELAY_TIME)
                    i+=1
            else:
                print ("Fail to select Common Settings")
                return False

    def enter_advanced_setting(self):
        """Click and enter advanced setting module in common settings interface
        @Return:True or False
        """
        print("Start to excute EnterAdvancedSetting")
        if self._device(**self._uip_advanced_settings).wait.exists(timeout=self._TIME_OUT):
            print ("Find Advanced Settings successfully")
            for i in range(self._CLICK_LOOP_TIME):
                if self._device(**self._uip_action_bar_title).wait.exists(timeout=self._TIME_OUT):
                    print ("Enter into Advanced Settings successfully")
                    return True
                else:
                    self._device(**self._uip_advanced_settings).click()
                    self._device.delay(self._DELAY_TIME)
                    i+=1
            else:
                print ("Fail to enter into Advanced Settings")
                return False
        else:
            print ("Not find Advanced Settings")
            return False







