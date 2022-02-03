# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/3/22
"""
import json
import pandas as pd
from .ult import run_cmd, _run_cmd, to_json


def get_user_dn_ls_from_file(fp: str) -> list:
    """
    return a list with user default (displayed) names

    :param fp:
    :return:
    """
    with open(fp, 'r') as f:
        result = f.readlines()
        for i in range(len(result)):
            u = result[i]
            result[i] = u.strip()

    return result


def get_all_user() -> list:
    """
    it will return all user (concise name) on the device, including some service name
    :return:
    """
    cmd = "getent passwd | awk -F: '{ print $1}'"
    return run_cmd(cmd)


def get_user_name(user: str):
    """
    return the Full (displayed) name of an user

    :param user:
    :return:
    """
    cmd = f"getent passwd {user} | cut -d ':' -f 5"
    return _run_cmd(cmd).strip()


def get_user_data() -> list:
    result = list()
    all_user = get_all_user()
    for i, user in enumerate(all_user, start=1):
        user_name = get_user_name(user)

        # strip system suffix characters
        if user_name[len(user_name) - 3:len(user_name)] == ',,,':
            user_name = user_name[0:len(user_name) - 3]

        user_data = {
            'index': i,
            'user': user,
            'name': user_name
        }

        result.append(user_data)

    return result


def map_user_data_with_user_dn_ls(user_dn_ls: list) -> list:
    """
    returned result:
    [
        {
            'uid': int,
            'default_name': str,
            'user': str,
            'created_by_cmd': bool,
        },
        {},
        ...,
        {}
    ]

    :param user_dn_ls:
    :return:
    """
    result = list()
    user_data = get_user_data()

    for i, user_dn in enumerate(user_dn_ls, start=1):
        for d in user_data:
            record = {
                'uid': i,
                'default_name': user_dn,
                'user': d['user'],
            }

            if user_dn == d['name']:
                record['created_by_cmd'] = False
                result.append(record)

            elif d['name'] == '' and d['user'] == user_dn:
                record['created_by_cmd'] = True
                result.append(record)

    return result


# >>>>>> Shortcut Functions >>>>>>
def get_q_user_data(user_dn_file_path: str) -> list:
    user_dn_ls = get_user_dn_ls_from_file(user_dn_file_path)
    return map_user_data_with_user_dn_ls(user_dn_ls)


def create_user_json(user_dn_file_path: str, save_fp='user_data.json'):
    user_q_data = get_q_user_data(user_dn_file_path)
    to_json(user_q_data, save_fp)


def get_user_json_str(user_dn_file_path: str) -> str:
    user_q_data = get_q_user_data(user_dn_file_path)
    return json.dumps(user_q_data)


def get_q_user_data_df(user_dn_file_path: str) -> pd.DataFrame:
    user_q_data = get_q_user_data(user_dn_file_path)
    return pd.DataFrame(user_q_data)


def create_user_csv(user_dn_file_path: str, save_fp='user_data.csv'):
    df = get_q_user_data_df(user_dn_file_path)
    df.to_csv(save_fp, index=False)
    
# <<<<<< Shortcut Functions <<<<<<
