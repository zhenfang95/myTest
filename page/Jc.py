#!/use/bin/env python
#coding:utf-8

import json
from utils.public import *
from utils.operationJson import  OperationJson
from utils.operationExcel import  OperationExcel
from utils.excel_data import *

operationJson=OperationJson()
operationExcel=OperationExcel()

def setSo(username="15217043402",password=123456):
	'''对请求的数据重新赋值'''
	dici1=json.loads(operationJson.getRequestsData(1))
	dici1['username']=username
	dici1['password']=password
	return dici1

def writeDatafile(fileName,content):
	'''获取的动态参数写入文件中'''
	with open(data_dir(fileName=fileName),'w') as f:
		f.write(content)

def getSessionId():
	'''读取session_id'''
	with open(data_dir(fileName='sessionid.md'),'r') as f:
		return f.read()

def getHeadersInfo():
	'''请求头添加登录参数'''
	headers=getHeadersValue()
	headers['AUTHORIZATION']=getSessionId()
	return headers

def setRelevance(row,orderSn):
	'''对有关联的参数重新赋值'''
	dict1=json.loads(operationJson.getRequestsData(row))
	dict1['orderSn']=orderSn
	return dict1

def getOrderId():
	'''读取订单编号'''
	with open(data_dir(fileName='orderId.md'),'r') as f:
		return f.read()

def getOrdersn():
	'''订单号提取处理'''
	list1=[]
	data=json.loads(getOrderId())  #反序列化把字符串转为列表
	for i in data:
		list1.append(i)
	return list1
