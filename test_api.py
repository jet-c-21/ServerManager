# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 3/16/22
"""
from pprint import pp
from server_manager import *

if __name__ == '__main__':
    x = get_service_user()
    # print(x)

    user_csv_sp = 'output/service_user.csv'
    # x.to_csv(user_csv_sp, index=False)

    y = get_user_data_sp()
    pp(y)

    # cmd = "awk -F: '($3<1000)&&($1!=\"root\")' /etc/passwd"
    # cmdexor._run_cmd(cmd)
