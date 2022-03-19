# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 3/16/22
"""
from pprint import pp
import server_manager as sm
import subprocess
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')



if __name__ == '__main__':
    pass
    # x = sm.user.get_user_env_var()
    # print(x)
    command = "su - ; echo"
    # p = subprocess.run(command, capture_output=True, shell=True, text=True)
    # print(p.stdout)

    cmd = 'echo  |-S su -; echo $USER'
    p = subprocess.Popen(cmd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)
    proc_out, proc_error = p.communicate()

    print(proc_out)
