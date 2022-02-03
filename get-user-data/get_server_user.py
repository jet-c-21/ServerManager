"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/25/21
"""
# coding: utf-8
import subprocess as sb
import os
import json
from pprint import pp


# def read_json(fp: str) -> dict:
#     return json.load(open(fp, 'r', encoding='utf-8'))
#
#
# def to_json(data, fp: str):
#     json.dump(data, open(fp, 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
#
#
# def _run_cmd(cmd: str) -> str:
#     return sb.check_output(cmd,
#                            stderr=sb.STDOUT,
#                            shell=True).decode('utf-8').strip()
#
#
# def run_cmd(cmd: str) -> list:
#     """
#     run command with parse
#     :param cmd:
#     :return:
#     """
#     return _run_cmd(cmd).split('\n')


# def get_all_user() -> list:
#     cmd = "getent passwd | awk -F: '{ print $1}'"
#     return run_cmd(cmd)
#
#
# def get_user_name(user: str):
#     cmd = f"getent passwd {user} | cut -d ':' -f 5"
#     return _run_cmd(cmd).strip()


# def get_user_data() -> list:
#     result = []
#     all_user = get_all_user()
#     for i, user in enumerate(all_user, start=1):
#         user_name = get_user_name(user)
#         if user_name[len(user_name) - 3:len(user_name)] == ',,,':
#             user_name = user_name[0:len(user_name) - 3]
#
#         user_data = {
#             'index': i,
#             'user': user,
#             'name': user_name
#         }
#         result.append(user_data)
#
#     return result


def get_user_json_data() -> str:
    return json.dumps(get_user_data())


# def get_udn_ls_from_file(fp: str) -> list:
#     with open(fp, 'r') as f:
#         result = f.readlines()
#         for i in range(len(result)):
#             u = result[i]
#             result[i] = u.strip()
#     return result


def map_data_with_udn_ls(udn_ls: list) -> list:
    result = list()
    user_data = get_user_data()
    for i, udn in enumerate(udn_ls, start=1):
        for d in user_data:
            if udn == d['name']:
                record = {
                    'uid': i,
                    'udn': udn,
                    'user': d['user'],
                    'user_name': udn,
                }
                result.append(record)

            elif d['name'] == '' and d['user'] == udn:
                record = {
                    'uid': i,
                    'udn': udn,
                    'user': d['user'],
                    'full_name': '',
                }
                result.append(record)

    return result


if __name__ == '__main__':
    # user defined name list
    UDN_LS = get_udn_ls_from_file('user_default_name.txt')
    USER_DATA = map_data_with_udn_ls(UDN_LS)
    to_json(USER_DATA, 'user_data.json')

    data_str = json.dumps(USER_DATA)
    print(data_str)
    print()
    pp(data_str)
