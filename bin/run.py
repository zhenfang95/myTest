#!/use/bin/env python
#coding:utf-8
import sys
sys.path.append("E:\\install\\jenkings\\workspace\\api_github\\")

import unittest
import os,time
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.operationExcel import OperationExcel

class Runner:
	def __init__(self):
		self.excel=OperationExcel()

	def getSuite(self):
		'''获取要执行的测试套件'''
		suite = unittest.TestLoader().discover(
			start_dir=sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests')),
			pattern='test_*.py',
			top_level_dir=None)
		return suite

	def getNowtime(self):
		'''获取当前时间'''
		now=time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))
		return now

	def getRun(self):
		'''生成测试报告'''
		filename=os.path.join(os.path.dirname(os.path.dirname(__file__)),'report',self.getNowtime()+'.html')
		ff=sys.path.append(filename)
		fp=open(ff,'wb')
		runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title='自动化测试报告',description='接口自动化测试')
		return runner

	def send_mail(self,smtp_server,sender,psw,receiver,port,content):
		'''
		发送邮件内容
		:param sender:发送邮件的人
		:param receiver:接受邮件的人
		:param content:邮件内容
		'''
		#找到生成最新报告的文件
		file_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'report')
		ff1=sys.path.append(file_path)
		lists=os.listdir(ff1)
		report_path=os.path.join(ff1,lists[-1])

		#定义邮件内容
		msg = MIMEMultipart()
		body = MIMEText(content, _subtype='plain', _charset='utf-8')
		msg['Subject'] = "接口自动化测试报告"
		msg["from"] = sender
		msg["to"] = psw
		msg.attach(body)
		#添加附件
		att = MIMEText(open(report_path, "rb").read(), "base64", "utf-8")
		att["Content-Type"] = "application/octet-stream"
		att["Content-Disposition"] = 'attachment; filename= "report.html"'
		msg.attach(att)
		try:
			smtp = smtplib.SMTP_SSL(smtp_server, port)
		except:
			smtp = smtplib.SMTP()
			smtp.connect(smtp_server, port)
		#用户名密码
		smtp.login(sender, psw)
		smtp.sendmail(sender, receiver, msg.as_string())
		smtp.quit()

	def main_run(self):
		'''执行测试用例'''
		self.getRun().run(self.getSuite())
		#统计测试用例成功率
		content='通过数：{0} 失败数：{1} 通过率：{2}'.format(
			self.excel.run_success_result(),
			self.excel.run_fail_result(),
			self.excel.run_pass_rate())
		#邮箱配置
		from config import readconfig
		smtp_server=readconfig.smtp_server
		sender=readconfig.sender
		psw=readconfig.psw
		receiver=readconfig.receiver
		port=readconfig.port
		self.send_mail(smtp_server,sender,psw,receiver,port,content)
		print('Please wait while the statistics test results are sent in the mail')

if __name__ == '__main__':
	Runner().main_run()