#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/8/5 15:49

import unittest
from base.method import Method,IsContent
from page.Jc import *
from utils.operationLog import MyLog

class HomeTest(unittest.TestCase):
    def setUp(self):
        self.obj=Method()
        self.p=IsContent()
        self.log=MyLog()
        self.excel=OperationExcel()

    def isContent(self,r,row):
        self.assertEqual(r.status_code,200)
        self.assertTrue(self.p.isContent(row=row,str2=r.text))

    def test_home_01(self):
        '''获取首页各类信息'''
        r=self.obj.method(6)
        self.isContent(r,6)
        self.excel.writeResult(6,'pass')

    def test_home_02(self):
        '''获取热门演出推荐列表'''
        r=self.obj.method(7)
        self.isContent(r,7)
        self.excel.writeResult(7,'pass')

    def test_home_03(self):
        '''获取巡演推荐列表'''
        r=self.obj.method(8)
        self.isContent(r,8)
        self.excel.writeResult(8,'pass')

    def test_home_04(self):
        '''获取首页楼层演出列表'''
        r=self.obj.method(9)
        self.isContent(r,9)
        self.excel.writeResult(9,'pass')

    def test_home_05(self):
        '''获取热门场馆列表'''
        r=self.obj.method(10)
        self.isContent(r,10)
        self.excel.writeResult(10,'pass')

    def test_home_06(self):
        '''为你推荐列表'''
        r=self.obj.method(11)
        self.isContent(r,11)
        self.excel.writeResult(11,'pass')



