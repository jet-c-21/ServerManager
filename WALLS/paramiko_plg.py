# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 3/17/22
"""
import paramiko
import time
import configparser
from shell_handeler import ShellHandler

cfg_path = '../config.cfg'

cfg = configparser.ConfigParser()
cfg.read(cfg_path)

host = cfg['host']['local']
user = cfg['user']['jet']
user_pwd = cfg['pwd']['j_pwd']
root_pwd = cfg['pwd']['root_pwd']

# shell = ShellHandler(host, user, user_pwd, 20)
# shin, shout, sherr = shell.execute('ls -a')
# print(shout)
# shin, shout, sherr = shell.execute('echo $USER')
# print(shout)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=user, password=user_pwd, port=20)
channel = ssh.invoke_shell()

time.sleep(1)
channel.recv(9999)
channel.send("\n")
time.sleep(1)

cmd_ls = ['whoami', 'ls']

for cmd in cmd_ls:
    channel.send(cmd + "\n")
    while not channel.recv_ready():  # Wait for the server to read and respond
        time.sleep(0.1)
    time.sleep(0.1)  # wait enough for writing to (hopefully) be finished
    output = channel.recv(9999)  # read in
    print(output.decode('utf-8'))
    print('=============')
    time.sleep(0.1)
channel.close()
