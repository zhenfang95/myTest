#!/use/bin/env python
#coding:utf-8

import  json
from utils.public import *
from utils.operationExcel import OperationExcel

class OperationJson:
	def __init__(self):
		self.excel=OperationExcel()

	def getReadJson(self):
		'''从json文件读取数据'''
		with open(data_dir(fileName='requestData.json'),encoding='utf-8') as fp:
			#反序列化，把json字符串转换为python数据类型
			data = json.load(fp)
			return data

	def getRequestsData(self,row):
		'''获取请求参数'''
		#序列化，把python数据类型转换为字典类型
		pydata=json.dumps(self.getReadJson()[self.excel.get_request_data(row=row)])
		return pydata
