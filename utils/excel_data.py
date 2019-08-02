#!/use/bin/env python
#coding:utf-8 

#Author:WuYa

class ExcelVariable:
	caseID=0
	url=2
	request_data=3
	method=4
	expect=5
	result=6

def getCaseID():
	return ExcelVariable.caseID

def getUrl():
	return ExcelVariable.url

def get_request_data():
	return ExcelVariable.request_data

def getMethod():
	return ExcelVariable.method

def getExpect():
	return ExcelVariable.expect

def getResult():
	return ExcelVariable.result

def getHeadersValue():
	'''获取请求头'''
	headers={
		'Content-Type':'application/x-www-form-urlencoded',
		'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
	}
	return headers
