#!/usr/bin/env python

# -*- coding:utf-8 -*-

s = """
---------------------------------------------------------------

author:moriweiji

Date:

python verison:2.7.11

---------------------------------------------------------------

"""
import smtplib
from email.mime.text import MIMEText

class Send_email(object):
    def __init__(self, smtp_server, mail_user, mail_pass, mail_postfix):

        """



        :param smtp_server: 邮件服务器

        :param mail_user: 邮件用户名

        :param mail_pass: 密码

        :param mail_postfix: 邮件域名后缀

        """
        # self.mailto_list = mail_list #['',]
        self.mail_host = smtp_server  # ""  # 设置服务器
        self.mail_user = mail_user  # ""  # 用户名
        self.mail_pass = mail_pass  # ""  # 口令
        self.mail_postfix = mail_postfix  # "189.cn"  # 发件箱的后缀
        # self.sub = sub #'server_run_complate'
        
    def send_mail(self, to_list, sub, content, charset):
        """

        :param to_list: 发送人员的列表 ['13316461250@189.cn',]

        :param sub: 发送的主题

        :param content: 发送内容

        :param charset:字符集 gb2312,utf-8,gbk

        :return: 返回Ture or False

        """
        me = "hello" + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        msg = MIMEText(content, _subtype='plain', _charset=charset)
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(me, to_list, msg.as_string())
            server.close()
            return True
        except Exception, e:
            print str(e)
            return False
