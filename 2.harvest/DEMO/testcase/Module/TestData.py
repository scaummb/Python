# -*- coding: UTF-8 -*-

import os
import sys
from ConfigParser import ConfigParser

class TestData(object):
    """Get a option value from a given section.

    @Discription: zhangzeliang@allwinnertech.com

    # This class can not be modified by anyone

    @Todo: None
    """

    def __init__(self, module):
        self._ConfigParserFilePath = os.path.dirname(sys.path[0])+ os.sep+"resource"+os.sep+"TestData.ini"
        if os.path.isfile(self._ConfigParserFilePath):
            # print "Find TestData.ini"
            pass
        else:
            assert False,"Not find %s" %self._ConfigParserFilePath
        self.commonconfig = ConfigParser()
        self.commonconfig.read(self._ConfigParserFilePath)
        self.testtype = self.commonconfig.get("DefaultOpen","TEST_TYPE").upper()
        self.testobject = self.commonconfig.get("DefaultOpen","TEST_OBJECT")
        self.module = module.capitalize()
        
    def get_int(self, section, option, filename, exc=0):
        """return an integer value for the named option.
        return exc if no the option. 
        """
        config = ConfigParser()
        try:
            config.read(os.path.dirname(sys.path[0])+os.sep+"resource"+ os.sep+filename + ".ini")
            return config.getint(section, option)
        except:
            return exc
        
    def get_str(self, section, option, filename, exc=None):
        """return an string value for the named option."""
        config = ConfigParser()
        try:
            config.read(os.path.dirname(sys.path[0])+os.sep+"resource"+ os.sep+filename + ".ini")
            return config.get(section,option)
        except:
            return exc
        
    def get_test_times(self):
        """return a dict with name:value for each option
        in the section.
        """
        config = ConfigParser()
        if self.testtype == "STRESS" :
            config.read(sys.path[0]+os.sep+self.testtype+"_"+self.testobject+".ini")
        item = config.items(self.module)
        return dict(item)

    def get_list(self, section, option, filename, exc=None):
        """return an list value for the named option."""
        config = ConfigParser()
        try:
            config.read(sys.path[0] + os.sep +filename + ".ini")
            config_str = config.get(section, option)
            return config_str.split(',')
        except:
            return exc

    def options(self, section, filename, exc=None):
        '''return list of configuration options for the named section
        '''
        
        config = ConfigParser()
        try:
            config.read(sys.path[0]+os.sep+"resource"+os.sep+filename+".ini")
            return(config.options(section))
        except:
            return(exc)

    def sections(self, filename, exc=None):
        '''return list of configuration options for the named section
        
        '''
        
        config = ConfigParser()
        try:
            config.read(sys.path[0]+os.sep +"resource"+os.sep+filename+".ini")
            return(config.sections())
        except:
            return(exc)
