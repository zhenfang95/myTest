#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/8/1 17:23

import os
import configparser

cur_path=os.path.dirname(os.path.realpath(__file__))
configPath=os.path.join(cur_path,'config.ini')
conf=configparser.ConfigParser()
conf.read(configPath)

smtp_server=conf.get("email","smtp_server")
sender=conf.get("email","sender")
psw=conf.get("email","psw")
receiver=conf.get("email","receiver")
port=conf.get("email","port")
