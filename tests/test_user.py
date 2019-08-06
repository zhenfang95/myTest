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
        order_sn=re.findall('order_sn":"(.+?)","',r.text)      #利用正则表达式提取所有订单编号
        writeDatafile(fileName='orderId.md',content=json.dumps(order_sn)) #序列化转为字符串写入

    def test_user_04(self):
        '''订单详情页验证'''
        #利用循环依次取出每个订单号
        for i in range(len(getOrdersn())):
            r=self.obj.method(15,data=setRelevance(row=15,orderSn=getOrdersn()[i]))
            self.isContent(r,15)
        self.excel.writeResult(15,'pass')

    def test_user_05(self):
        '''电子票夹验证'''
        r=self.obj.method(16)
        self.isContent(r,16)
        self.excel.writeResult(16,'pass')

    def test_user_06(self):
        '''我的卡包列表验证'''
        r=self.obj.method(17)
        self.isContent(r,17)
        self.excel.writeResult(17,'pass')

if __name__ == "__main__":
    unittest.main()
