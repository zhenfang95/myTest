#!/use/bin/env python
#coding:utf-8

import json
from utils.public import *
from utils.operationJson import  OperationJson
from utils.operationExcel import  OperationExcel
from utils.excel_data import *

operationJson=OperationJson()
operationExcel=OperationExcel()

def setSo(username="13097888019",password=123456):
	'''对请求的数据重新赋值'''
	dici1=json.loads(operationJson.getRequestsData(1))
	dici1['username']=username
	dici1['password']=password
	return dici1

def writeSessionId(content):
	'''把sessionid写入文件中'''
	with open(data_dir(fileName='sessionid.md'),'w') as f:
		f.write(content)

def getSessionId():
	'''获取sessionid'''
	with open(data_dir(fileName='sessionid.md'),'r') as f:
		return f.read()

def getHeadersInfo():
	'''请求头添加登录参数'''
	headers=getHeadersValue()
	headers['AUTHORIZATION']=getSessionId()
	return headers

def getUrl():
	'''当相同url存在多个参数的处理方法'''
	listUrl=[]
	for item in getSessionId():
		url='https://www.xxx.com/xxx/{0}.html'.format(item)
		listUrl.append(url)
	return listUrl

def setRelevance(row,orderSn):
	'''对有关联的参数重新赋值'''
	dict1=json.loads(operationJson.getRequestsData(row))
	dict1['orderSn']=orderSn
	return dict1


