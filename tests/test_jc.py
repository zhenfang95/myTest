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

class JcTest(unittest.TestCase):
	def setUp(self):
		self.obj=Method()
		self.p=IsContent()
		self.execl=OperationExcel()
		self.operationJson=OperationJson()
		self.log=MyLog()

	def statusCode(self,r):
		self.assertEqual(r.status_code, 200)
		#self.assertEqual(r.json()['code'], 1)

	def isContent(self,r,row):
		self.statusCode(r=r)
		self.assertTrue(self.p.isContent(row=row,str2=r.text))

	def test_001(self):
		'''正确的账号密码登录'''
		self.log.infoLog('-----正确的账号密码登录-----')
		r = self.obj.post(1,data=setSo())
		self.log.infoLog('登录结果：%s' % r.json())
		self.isContent(r,1)
		self.execl.writeResult(1,'pass')   #测试结果写到excel
		#cookies= requests.utils.dict_from_cookiejar(r.cookies)  #把cookies转为字典类型
		writeSessionId(r.cookies['juooo_sessionid'])  #提取sessionid
		self.log.infoLog('提取sessionid成功，sessionid为：%s'%r.cookies['juooo_sessionid'])

	def test_002(self):
		'''正确的账号错误的密码登录'''
		self.log.infoLog('-----正确的账号错误的密码登录-----')
		r=self.obj.post(2,data=setSo(password=1230))
		self.log.infoLog('登录结果：%s' % r.json())
		self.isContent(r,2)
		self.execl.writeResult(2, 'pass')

	def test_003(self):
		'''错误的账号正确密码登录'''
		self.log.infoLog('-----错误的账号正确密码登录-----')
		r=self.obj.post(3,data=setSo(username='130645501500'))
		self.log.infoLog('登录结果：%s' % r.json())
		self.isContent(r,3)
		self.execl.writeResult(3, 'pass')

	def test_004(self):
		'''错误的账号错误的密码登录'''
		self.log.infoLog('-----错误的账号错误的密码登录-----')
		r=self.obj.post(4,data=setSo(username='130645512599',password=123))
		self.log.infoLog('登录结果：%s' % r.json())
		self.isContent(r,4)
		self.execl.writeResult(4, 'pass')

	def test_005(self):
		'''账号密码为空登录'''
		self.log.infoLog('-----账号密码为空登录-----')
		r=self.obj.post(5,data=setSo(username='',password=''))
		self.log.infoLog('登录结果：%s' % r.json())
		self.isContent(r,5)
		self.execl.writeResult(5, 'pass')

	def test_006(self):
		'''个人中心'''
		r = self.obj.method(6)
		self.isContent(r,6)
		self.execl.writeResult(6, 'pass')

	def test_007(self):
		'''我的订单'''
		r = self.obj.method(7)
		self.isContent(r,7)
		self.execl.writeResult(7, 'pass')

if __name__ == '__main__':
	unittest.main(verbosity=2)
