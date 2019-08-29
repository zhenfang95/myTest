#!/use/bin/env python
#coding:utf-8

import  unittest
import  requests
from base.method import Method,IsContent
from utils.public import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson
from page.Jc import *
from utils.operationLog import MyLog

class LoginTest(unittest.TestCase):
	def setUp(self):
		self.obj=Method()
		self.p=IsContent()
		self.execl=OperationExcel()
		self.operationJson=OperationJson()
		self.log=MyLog()

	def isContent(self,r,row):
		self.assertEqual(r.status_code, 200)
		self.assertTrue(self.p.isContent(row=row,str2=r.text))

	def test_login_01(self):
		'''正确的账号密码登录'''
		r = self.obj.post(1,data=setSo())
		self.isContent(r,1)
		self.execl.writeResult(1,'pass')   #测试结果写到excel
		#cookies= requests.utils.dict_from_cookiejar(r.cookies)  #把cookies转为字典类型
		#提取sessionid并写入文件中
		writeDatafile(fileName='sessionid.md',content=r.cookies['juooo_sessionid'])

	def test_login_02(self):
		'''正确的账号错误的密码登录'''
		r=self.obj.post(2,data=setSo(password=1230))
		self.isContent(r,2)
		self.execl.writeResult(2, 'pass')

	def test_login_03(self):
		'''错误的账号正确密码登录'''
		r=self.obj.post(3,data=setSo(username='130645501500'))
		self.isContent(r,3)
		self.execl.writeResult(3, 'pass')

	def test_login_04(self):
		'''错误的账号错误的密码登录'''
		r=self.obj.post(4,data=setSo(username='130645512599',password=123))
		self.isContent(r,4)
		self.execl.writeResult(4, 'pass')

	def test_login_05(self):
		'''账号密码为空登录'''
		r=self.obj.post(5,data=setSo(username='',password=''))
		self.isContent(r,5)
		self.execl.writeResult(5, 'pass')

if __name__ == '__main__':
	unittest.main(verbosity=2)
