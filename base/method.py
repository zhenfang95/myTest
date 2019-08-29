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
				data=data,
				headers=getHeadersValue(),
				timeout=6)
			self.log.infoLog('接口%s请求成功，请求方式：post，请求参数：%s' %(self.excel.getCaseID(row),data))
			return r
		except Exception as e:
			self.log.errorLog('接口%s请求错误,原因：%s'%(self.excel.getCaseID(row),e))
			raise  RuntimeError('接口请求发生未知的错误')

	def get(self,row,params=None):
		try:
			r=requests.get(url=self.excel.getUrl(row),
						params=params,
						headers=getHeadersValue(),
						timeout=6)
			self.log.infoLog('接口%s请求成功，请求方式：get，请求参数：%s' %(self.excel.getCaseID(row),params))
			return r
		except Exception as e:
			self.log.errorLog('接口%s请求错误,原因：%s'%(self.excel.getCaseID(row),e))
			raise RuntimeError('接口请求发生未知错误')

	def method(self,row,data=None,params=None):
		method=self.excel.getMethod(row)
		if method == 'post':
			r=requests.post(
				url=self.excel.getUrl(row),
				data=data,
				headers=getHeadersInfo(),
				timeout=6)
			self.log.infoLog('接口%s请求成功，请求方式：post，请求参数：%s' %(self.excel.getCaseID(row),data))
			return r
		elif method == 'get':
				r=requests.get(
					url=self.excel.getUrl(row),
					params=params,
					headers=getHeadersInfo(),
					timeout=6)
				self.log.infoLog('接口%s请求成功，请求方式：get，请求参数：%s' %(self.excel.getCaseID(row),params))
				return r
		else:
			self.log.errorLog('接口请求方式不正确')


#通过预期结果断言
class IsContent:
	def __init__(self):
		self.excel=OperationExcel()
		self.log=MyLog()

	def isContent(self,row,str2):
		flag=None
		if self.excel.getExpect(row=row) in str2:
			flag=True
			self.log.infoLog('%s接口通过预期结果断言成功'%self.excel.getCaseID(row))
		else:
			flag=False
			self.log.errorLog('%s接口通过预期结果断言失败'%self.excel.getCaseID(row))
		return flag
