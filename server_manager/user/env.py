# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 3/17/22
"""
import subprocess
from ..run import cmdexor


def get_user_env_var():
    su_pwd = ''

    # p = subprocess.call('echo $HOME', shell=True)
    # print(p)
    # print(type(p))

    cmd = f"echo {su_pwd} | sudo -S su - | echo $USER"
    # cmd = f"echo {su_pwd} | sudo -S grep -e \"$pattern\" /home/*/.bash_history"
    return cmdexor._run_cmd_by_open_proc(cmd)

    # return cmdexor.run_cmd_popen(cmd)
