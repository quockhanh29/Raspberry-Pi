#-*- coding:utf-8 -*-

import smtplib
from email.utils import formatdate
from email.mime.text import MIMEText

SMTP_SERVER = "www.wincloud.site"
PORT_NUMBER = 587

mail_to = ""

mail_from ="students@wincloud.site"

subject = "RaspberryPi からメール"

body = "IoT実行です"

msg = MIMEText(body, "plain")

msg["From"] = mail_from
msg["To"] = mail_to
msg["Date"] = formatdate()
msg["Subject"] = subject

smtp_obj = smtplib.SMTP(SMTP_SERVER, PORT_NUMBER)
smtp_obj.ehlo()
smtp_obj.login("students","winstudents")
smtp_obj.sendmail(mail_from, mail_to, msg.as_string())
smtp_obj.close()
