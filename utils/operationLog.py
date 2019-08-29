#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/8/1 11:24

import time,os
import logging

class MyLog:
    def __init__(self):
        title='接口自动化测试'
        day=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        path=os.path.dirname(os.path.dirname(__file__))+'\\logs'  #日志存放路径
        file=os.path.join(path,(day+'.log'))  #创建日志文件
        self.logger=logging.Logger(title)
        self.logger.setLevel(logging.DEBUG)   #设置log为最高级别
        self.logfile=logging.FileHandler(file,encoding='utf-8')  #日志输出到文件
        self.logfile.setLevel(logging.DEBUG)
        # self.control=logging.StreamHandler() #日志输出到控制台
        # self.control.setLevel(logging.DEBUG)
        #设置日志输出格式
        self.formater=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s:%(message)s')
        self.logfile.setFormatter(self.formater)
        #self.control.setFormatter(self.formater)
        self.logger.addHandler(self.logfile)
        #self.logger.addHandler(self.control)

    def debugLog(self,message):
        self.logger.debug(message)

    def infoLog(self,message):
        self.logger.info(message)

    def warnLog(self,message):
        self.logger.warning(message)

    def errorLog(self,message):
        self.logger.error(message)
