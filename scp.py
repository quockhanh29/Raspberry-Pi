# -*- coding:utf-8 -*-

import pexpect

local_filename = './scp2.txt'

ID = 'students'
PASSWORD = 'winstudents'
HOST = 'www.wincloud.site'
DIR = 'public_html'

students_dir = 'THD9C384ps34'

server_filename = 'scp2.txt'
print("SCPコマンドを実行します")

scp_command = 'scp ' + local_filename
scp_command = scp_command + ' ' + ID + '@' + HOST + ':' + DIR + '/' + students_dir + '/' + server_filename

command = pexpect.spawn(scp_command)
command.expect('(?i)password')
command.sendline(PASSWORD)
command.expect(pexpect.EOF)

print("SCPコマンドが実行されました")

