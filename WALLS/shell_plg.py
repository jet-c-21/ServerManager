# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 3/19/22
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


def print_output(d):
    print('>' * 20)
    for _ in d:
        print(_)
    print('<' * 20)


shell = ShellHandler(host, user, user_pwd, 20)
shin, shout, sherr = shell.execute(f"echo '{user_pwd}' | sudo -S su root")
print_output(shout)

# shin.write(root_pwd + '\n')
# shin.flush()

shin, shout, sherr = shell.execute("echo RESULT: $USER")
print_output(shout)
