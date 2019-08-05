#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/8/5 16:31

import unittest
import re
from base.method import Method,IsContent
from page.Jc import *
from utils.operationLog import MyLog

class UserTest(unittest.TestCase):
    def setUp(self):
        self.obj=Method()
        self.p=IsContent()
        self.log=MyLog()
        self.excel=OperationExcel()
        self.operJson=OperationJson()

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

    def test_user_03(self):
        '''获取我的订单列表'''
        r=self.obj.method(14,data=self.operJson.getRequestsData(14))
        self.isContent(r,14)
        self.excel.writeResult(14,'pass')
        order_sn=re.findall('order_sn":(.+?),"',r.text)    #利用正则表达式提取订单编号
        return order_sn[0]

    def test_user_04(self):
        '''订单详情'''
        r=self.obj.method(15,data=setRelevance(row=15,orderSn=eval(self.test_user_03())))  #eval-->把字符串转为字典
        self.isContent(r,15)
        self.excel.writeResult(15,'pass')

if __name__ == "__main__":
    unittest.main()
