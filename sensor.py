# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time
import subprocess
import pexpect
import smtplib
from email import encoders
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

PIN = 14

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

while True:
    if (GPIO.input(PIN) == GPIO.HIGH):
        print("人体を感知しました")
        break

    print("センサー感知中")
    time.sleep(1)
#camera
image_file ="/home/pi/capture.jpg"
image_command = "raspistill -t 1000 -o " + image_file
subprocess.call(image_command, shell = True)

wavfile = "/home/pi/alert.wav"
command = "aplay " + wavfile
subprocess.call(command, shell=True)

wavfile ="/home/pi/security.wav"
command ="aplay " + wavfile
subprocess.call(command, shell=True)

#web cloud
ID = 'students'
PASSWORD = 'winstudents'
HOST = 'www.wincloud.site'
DIR = 'public_html'

students_dir = 'THD9C384ps34'

server_filename = 'capture.jpg'
local_filename = './capture.jpg'


scp_command = 'scp ' + local_filename
scp_command = scp_command + ' ' + ID + '@' + HOST + ':' + DIR + '/' + students_dir + '/' + server_filename

command = pexpect.spawn(scp_command)
command.expect('(?i)password')
command.sendline(PASSWORD)
command.expect(pexpect.EOF)

#line
ACCESS_TOKEN = "DDpYCJat8srwwtkOSoX8LgCAMscjeg97xLuYl4eSZkn"
# メッセージ
MESSAGE = "防犯システムが作動しました。写真url :http://" + HOST + "/~students/" + students_dir + "/" + server_filename

# 通知コマンド
command = "curl"
command = command + " -X POST"
command = command + " -H 'Authorization: Bearer " + ACCESS_TOKEN + "'"
command = command + " -F 'message=" + MESSAGE + "'"
command = command + " https://notify-api.line.me/api/notify"
# コマンド実行
subprocess.call(command, shell=True)

#mail
SMTP_SERVER = "www.wincloud.site"
PORT_NUMBER = 587

mail_to = "gmail.com"

mail_from ="students@wincloud.site"

subject = "防犯システムが作動しました。"

body = "urlから写真を確認ください。"
body = body + "http://" + HOST + "/~students/" + students_dir + "/" + server_filename

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

