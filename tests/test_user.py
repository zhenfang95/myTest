#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/8/5 16:31

import unittest
from base.method import Method,IsContent
from page.Jc import *
from utils.operationLog import MyLog

class UserTest(unittest.TestCase):
    def setUp(self):
        self.obj=Method()
        self.p=IsContent()
        self.log=MyLog()
        self.excel=OperationExcel()

    def isContent(self,r,row):
        self.assertEqual(r.status_code,200)
        self.assertTrue(self.p.isContent(row=row,str2=r.text))

    def test_user_01(self):
        '''获取个人信息'''
        r=self.obj.method(12)
        self.isContent(r,12)
        self.excel.writeResult(12,'pass')

    def test_user_02(self):
        '''获取菜单配置数据'''
        r=self.obj.method(13)
        self.isContent(r,13)
        self.excel.writeResult(13,'pass')