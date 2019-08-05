#!/use/bin/env python
#coding:utf-8

import requests
from utils.excel_data import *
from page.Jc import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson
from utils.operationLog import MyLog

operationExcel = OperationExcel()

class Method:
	def __init__(self):
		self.operationJson=OperationJson()
		self.excel=OperationExcel()
		self.log=MyLog()

	def post(self,row,data=None):
		try:
			r=requests.post(
				url=self.excel.getUrl(row),
				data=data,   #获取到的请求参数默认为str类型，把data转换为dict类型
				headers=getHeadersValue(),
				timeout=6)
			return r
		except Exception as e:
			self.log.errorLog('接口请求发生未知的错误,原因：%s'%e)
			raise  RuntimeError('接口请求发生未知的错误')

	def get(self,row,params=None):
		r=requests.get(url=self.excel.getUrl(row),
					params=params,
					headers=getHeadersValue(),
					timeout=6)
		return r

	def method(self,row,data=None,params=None):
		method=self.excel.getMethod(row)
		if method == 'post':
			r=requests.post(
				url=self.excel.getUrl(row),
				data=data,
				headers=getHeadersInfo(),
				timeout=6)
			return r
		elif method == 'get':
				r=requests.get(
					url=self.excel.getUrl(row),
					params=params,
					headers=getHeadersInfo(),
					timeout=6)
				return r
		else:
			self.log.errorLog('接口请求方式不正确')


#通过预期结果断言
class IsContent:
	def __init__(self):
		self.excel=OperationExcel()

	def isContent(self,row,str2):
		flag=None
		if self.excel.getExpect(row=row) in str2:
			flag=True
		else:
			flag=False
		return flag
