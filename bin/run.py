#!/use/bin/env python
#coding:utf-8
import sys
sys.path.append("E:\\install\\jenkings\\workspace\\api_github\\")
import unittest
import os,time
from utils.operationLog import MyLog
from config import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sys.path.append(os.path.dirname(os.path.dirname(__file__))+'\\utils')
from utils.operationExcel import OperationExcel
sys.path.append(os.path.dirname(os.path.dirname(__file__))+'\\tests')
sys.path.append(os.path.dirname(os.path.dirname(__file__))+'\\report')

class Runner:
	def __init__(self):
		self.excel=OperationExcel()
		self.log=MyLog()

	def getSuite(self):
		'''获取要执行的测试套件'''
		suite = unittest.TestLoader().discover(
			start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)),'tests'),
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
		fp=open(filename,'wb')
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
		lists=os.listdir(file_path)
		report_path=os.path.join(file_path,lists[-1])

		#定义邮件内容
		msg = MIMEMultipart()
		body = MIMEText(content, _subtype='plain', _charset='utf-8')
		self.log.infoLog('添加邮件内容：%s'%content)
		msg['Subject'] = "接口自动化测试报告"
		msg["from"] = sender
		self.log.infoLog('发件人邮箱：%s'%sender)
		msg["to"] = psw
		msg.attach(body)
		#添加附件
		att = MIMEText(open(report_path, "rb").read(), "base64", "utf-8")
		self.log.infoLog('读取附件')
		att["Content-Type"] = "application/octet-stream"
		att["Content-Disposition"] = 'attachment; filename= "report.html"'
		msg.attach(att)
		self.log.infoLog('添加邮件附件')
		try:
			smtp = smtplib.SMTP_SSL(smtp_server, port)
			self.log.infoLog('连接邮箱smtp服务')
		except:
			smtp = smtplib.SMTP()
			smtp.connect(smtp_server, port)
			self.log.infoLog('连接邮箱smtp服务')
		self.log.infoLog('smtp服务连接成功')
		#用户名密码
		smtp.login(sender, psw)
		smtp.sendmail(sender, receiver, msg.as_string())
		self.log.infoLog('收件人邮箱：%s'%receiver)
		smtp.quit()

	def main_run(self):
		'''执行测试用例'''
		self.getRun().run(self.getSuite())
		self.log.infoLog('-------------------------测试用例执行完毕-----------------------')
		self.log.infoLog('已生成html报告。。。')
		#统计测试用例成功率
		content='测试用例执行情况：通过数：{0} 失败数：{1} 通过率：{2} \n附件为-->接口自动化测试报告<--'.format(
			self.excel.run_success_result(),
			self.excel.run_fail_result(),
			self.excel.run_pass_rate())
		self.log.infoLog('统计测试用例执行成功率完成。。。')
		#邮箱配置
		from config import readconfig
		smtp_server=readconfig.smtp_server
		sender=readconfig.sender
		psw=readconfig.psw
		receiver=readconfig.receiver
		port=readconfig.port
		self.log.infoLog('----------------开始发送邮件----------------------')
		self.send_mail(smtp_server,sender,psw,receiver,port,content)
		print('Please wait while the statistics test results are sent in the mail')
		self.log.infoLog('----------------邮件发送成功----------------------')

if __name__ == '__main__':
	Runner().main_run()