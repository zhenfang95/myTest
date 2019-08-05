#!/use/bin/env python
#coding:utf-8

import xlrd
from xlutils.copy import copy
from utils.public import *
from utils.excel_data import *


class OperationExcel:
	def getExcel(self):
		db=xlrd.open_workbook(data_dir('data','data.xls'))
		sheet=db.sheet_by_index(0)
		return sheet

	def get_rows(self):
		'''获取excel的行数'''
		return self.getExcel().nrows

	def get_row_cel(self,row,col):
		'''获取单元格的内容'''
		return self.getExcel().cell_value(row,col)

	def getCaseID(self,row):
		'''获取测试ID'''
		return self.get_row_cel(row,getCaseID())

	def getUrl(self,row):
		'''获取请求地址'''
		return self.get_row_cel(row,getUrl())

	def get_request_data(self,row):
		'''获取请求参数'''
		return self.get_row_cel(row, get_request_data())

	def getMethod(self,row):
		'''获取请求方式'''
		return self.get_row_cel(row,getMethod())

	def getExpect(self,row):
		'''获取期望结果'''
		return self.get_row_cel(row,getExpect())

	def getResult(self,row):
		'''获取实际的结果'''
		return self.get_row_cel(row,getResult())

	def writeResult(self,row,content):
		'''测试结果写到文件中'''
		col=getResult()
		work =xlrd.open_workbook(data_dir('data','data.xls'))  #打开表
		old_content = copy(work)     #利用xlutils.copy下的copy函数复制
		ws = old_content.get_sheet(0)   #获取表单0
		ws.write(row,col,content)     ##改变（row,col）的值
		old_content.save(data_dir("data","data.xls"))   #保存文件

	def run_success_result(self):
		'''获取执行成功的用例数'''
		pass_count=[]
		fail_count=None
		for i in range(1,self.get_rows()):
			if self.getResult(i)=='pass':
				pass_count.append(i)
		return int(len(pass_count))

	def run_fail_result(self):
		'''获取执行失败的用例数'''
		return int((self.get_rows()-1)-self.run_success_result())  #总数减去成功数

	def run_pass_rate(self):
		'''测试结果通过率'''
		rate=''
		if self.run_fail_result()==0:
			rate='100%'
		elif self.run_fail_result()!=0:
			rate=str(int(self.run_success_result()/int(self.get_rows()-1)*100))+'%'
		return rate

	def getRows(self):
		row=[]
		for item in range(2,self.get_rows()):
			row.append(item)
		return row

# p=OperationExcel()
# print(p.run_success_result())
