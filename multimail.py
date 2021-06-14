#-*- coding:utf-8 -*-

import smtplib
from email import encoders
from email.utils import formatdate
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "www.wincloud.site"
PORT_NUMBER = 587

mail_to = "gmail.com"

mail_from ="students@wincloud.site"

subject = "RaspberryPi からメール"

body = "添付ファイルmail.txtを確認してください。"

msg = MIMEText(body, "plain")
msg = MIMEMultipart()
msg["From"] = mail_from
msg["To"] = mail_to
msg["Date"] = formatdate()
msg["Subject"] = subject

#本文
body = MIMEText(body)
msg.attach(body)

# 添付ファイル設定(mail.txtファイルを添付)
mime={'type':'text', 'subtype':'plain'}
attach_file={'name':'mail.txt', 'path':'./mail.txt'}

# 添付ファイル
mimebase_obj = MIMEBase(mime['type'],mime['subtype'])
file_obj = open(attach_file['path'])
mimebase_obj.set_payload(file_obj.read())
file_obj.close()
mimebase_obj.add_header("Content-Disposition","attachment", filename=attach_file['name'])
msg.attach(mimebase_obj)

smtp_obj = smtplib.SMTP(SMTP_SERVER, PORT_NUMBER)
smtp_obj.ehlo()
smtp_obj.login("students","winstudents")
smtp_obj.sendmail(mail_from, mail_to, msg.as_string())
smtp_obj.close()
