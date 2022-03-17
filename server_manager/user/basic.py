# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 3/17/22
"""
from ..run import cmdexor
import pandas as pd


def _get_user_df(user_data: list) -> pd.DataFrame:
    df = pd.DataFrame(columns=[
        'Username',  # <$1>, It is used when user logs in. It should be between 1 and 32 characters in length
        'UID',  # <$3>, User ID number
        'GID',  # <$4>, User’s group ID number (GID)
        'Shell',  # <$7>, The absolute path of a command or shell (/bin/bash)
        'HDIR',  # <$6>, User home directory
        'XPWD',  # <$2>, Encrypted password (x means that the password is stored in the /etc/shadow file)
        'FullName',  # <f1-$5>, User's full name (or application name, if the account is for a program)
        'RoomNumber',  # <f2-$5>, Building and room number or contact person
        'WorkPhone',  # <f3-$5>, Office telephone number
        'HomePhone',  # <f4-$5>, Home telephone number
        'Other',  # <f5-$5>, Any other contact information (pager number, fax, external e-mail address, etc.)
        'GECOS',  # <$5>, User Info
    ])

    for r in user_data:
        tokens = r.split('$')
        user_name = tokens[0]
        x_pwd = tokens[1]
        uid = tokens[2]
        gid = tokens[3]
        gecos = tokens[4]

        gecos_tokens = gecos.split(',')
        full_name = gecos_tokens[0]

        if 1 < len(gecos_tokens):
            room_number = gecos_tokens[1]
        else:
            room_number = ''

        if 2 < len(gecos_tokens):
            work_phone = gecos_tokens[2]
        else:
            work_phone = ''

        if 3 < len(gecos_tokens):
            home_phone = gecos_tokens[3]
        else:
            home_phone = ''

        if 4 < len(gecos_tokens):
            other = gecos_tokens[4]
        else:
            other = ''

        home_dir = tokens[5]
        shell = tokens[6]

        df.loc[len(df)] = [
            user_name, uid, gid, shell, home_dir, x_pwd,
            full_name, room_number, work_phone, home_phone, other, gecos
        ]

    df['UID'] = df['UID'].astype(int)
    df['GID'] = df['GID'].astype(int)

    return df


def _get_user_data(user_class: int):
    if user_class == 1:
        cmd = "awk 'BEGIN{FS=\":\"; OFS=\"$\"} ($3>=1000) && ($1!=\"nobody\") {print $1, $2, $3, $4, $5, $6, $7}' /etc/passwd"
    elif user_class == 2:
        cmd = "awk 'BEGIN{FS=\":\"; OFS=\"$\"} ($3>=1000) && ($1!=\"nobody\") || ($1==\"root\") {print $1, $2, $3, $4, $5, $6, $7}' /etc/passwd"
    elif user_class == 3:
        cmd = "awk 'BEGIN{FS=\":\"; OFS=\"$\"} ($3<1000) && ($1!=\"root\") {print $1, $2, $3, $4, $5, $6, $7}' /etc/passwd"
    else:
        cmd = "awk 'BEGIN{FS=\":\"; OFS=\"$\"} {print $1, $2, $3, $4, $5, $6, $7}' /etc/passwd"

    return cmdexor.run_cmd(cmd)


def get_user(sort_by='UID'):
    user_data = _get_user_data(1)
    user_df = _get_user_df(user_data)
    user_df = user_df.sort_values(by=[sort_by])
    return user_df


def get_service_user(sort_by='UID'):
    user_data = _get_user_data(2)
    user_df = _get_user_df(user_data)
    user_df = user_df.sort_values(by=[sort_by])
    return user_df


def get_system_user(sort_by='UID'):
    user_data = _get_user_data(3)
    user_df = _get_user_df(user_data)
    user_df = user_df.sort_values(by=[sort_by])
    return user_df


def get_user_all(sort_by='UID'):
    user_data = _get_user_data(4)
    user_df = _get_user_df(user_data)
    user_df = user_df.sort_values(by=[sort_by])
    return user_df
