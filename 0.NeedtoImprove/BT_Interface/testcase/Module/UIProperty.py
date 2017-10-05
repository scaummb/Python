#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import xml.dom.minidom

class UiProperty(object):
    """About setting module operation with module setting interfaces

    @Discription: zhangzeliang@allwinnertech.com

    # This class can not be modified by anyone

    @Todo: None
    """

    def __init__(self):
        self._UIMappingFilePath = os.path.dirname(sys.path[0])+  os.sep+"resource"+os.sep+"UIProperty.xml"
        if os.path.isfile(self._UIMappingFilePath):
            print("Find UIProperty.xml")
        else:
            assert False,"Not find %s" %self._UIMappingFilePath
        self._ElementList = ["text",
                             "textMatches",
                             "textContains",
                             "textStartsWith",
                             "resourceId",
                             "resourceIdMatches",
                             "className",
                             "classNameMatches",
                             "description",
                             "descriptionContains",
                             "descriptionMatches",
                             "descriptionStartsWith",
                             "packageName",
                             "packageNameMatches",
                             "index",
                             "instance"
                             ]
        print ("Start to Get UI Properties")

    def GetUIProperty(self, UiLogicName):
        self._DOMTree = xml.dom.minidom.parse(self._UIMappingFilePath)
        self._collection = self._DOMTree.documentElement
        self._elements = self._collection.getElementsByTagName("MappingElement")
        self._ElementListDict = {}
        for element in self._elements:
            if element.hasAttribute("UiLogic"):
                if element.getAttribute("UiLogic") == UiLogicName:
                    for item in self._ElementList:
                        if element.hasAttribute(item):
                            if element.getAttribute(item) != "":
                                if item == "index":
                                    self._ElementListDict[item] = int(element.getAttribute(item))
                                else:
                                    self._ElementListDict[item] = element.getAttribute(item)
                    return self._ElementListDict




