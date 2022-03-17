# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 3/17/22
"""
import paramiko
import time

host = 'localhost'
username = 'jet'
password = ''

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.load_system_host_keys()
ssh.connect(hostname=host, username=username, password=password, port=20)

stdin, stdout, stderr = ssh.exec_command('su root')
stdin: paramiko.ChannelStdinFile
stdout: paramiko.ChannelFile
stderr: paramiko.ChannelStderrFile
time.sleep(.1)

# ssh.exec_command('echo $USER')

stdin.write('' + '\n')
stdin.flush()
time.sleep(.1)

stdin, stdout, stderr = ssh.exec_command('echo $USER')

print(stdout.readlines())
ssh.close()


