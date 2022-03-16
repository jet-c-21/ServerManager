# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/3/22
"""
from .run import cmdexor
import pandas as pd


def _get_user_df(user_data: list):
    df = pd.DataFrame(columns=[
        'Username',  # <$1>, It is used when user logs in. It should be between 1 and 32 characters in length
        'UID',  # <$3>, User ID number
        'GID',  # <$4>, User’s group ID number (GID)
        'Shell',  # <$7>, The absolute path of a command or shell (/bin/bash)
        'HDIR',  # <$6>, User home directory
        'XPWD',  # <$2>, Encrypted password (x means that the password is stored in the /etc/shadow file)
        'FullName',  # <f1-$5>, User's full name (or application name, if the account is for a program)
        'Contact',  # <f2-$5>, Building and room number or contact person
        'OfficeTel',  # <f3-$5>, Office telephone number
        'HomeTel',  # <f4-$5>, Home telephone number
        'OtherContact',  # <f5-$5>, Any other contact information (pager number, fax, external e-mail address, etc.)
        'GECOS',  # <$5>, User Info
    ])

    for r in user_data:
        tokens = r.split(' ')
        user_name = tokens[0]
        x_pwd = tokens[1]
        uid = tokens[2]
        gid = tokens[3]
        gecos = tokens[4]

        gecos_tokens = gecos.split(',')
        full_name = gecos_tokens[0]

        if 1 < len(gecos_tokens):
            contact = gecos_tokens[1]
        else:
            contact = ''

        if 2 < len(gecos_tokens):
            office_tel = gecos_tokens[2]
        else:
            office_tel = ''

        if 3 < len(gecos_tokens):
            home_tel = gecos_tokens[3]
        else:
            home_tel = ''

        if 4 < len(gecos_tokens):
            other_contact = gecos_tokens[4]
        else:
            other_contact = ''

        home_dir = tokens[5]
        shell = tokens[6]

        df.loc[len(df)] = [
            user_name, uid, gid, shell, home_dir, x_pwd,
            full_name, contact, office_tel, home_tel, other_contact, gecos
        ]

    return df


def get_system_user():
    # cmd = "awk -F: '($3<1000)&&($1!=\"root\") {print $1, $2, $3, $4, $5, $6, $7}' /etc/passwd"
    cmd = "awk -F: '($3<1000) {print $1, $2, $3, $4, $5, $6, $7}' /etc/passwd"
    user_data = cmdexor.run_cmd(cmd)

    return _get_user_df(user_data)


def get_service_user():
    cmd = "awk -F: '($3>=1000)&&($1!=\"nobody\"){print $1, $2, $3, $4, $5, $6, $7}' /etc/passwd"
    user_data = cmdexor.run_cmd(cmd)

    return _get_user_df(user_data)


def get_user_data():
    cmd = "awk -F: '($3>=1000)&&($1!=\"nobody\")' /etc/passwd"
    user_data = cmdexor.run_cmd(cmd)

    return user_data


def get_user_data_sp():
    cmd = "awk -F: '($3>=1000)&&($1!=\"nobody\"){print $1, \"$$$\", $2, $3, $4, $5, $6, $7}' /etc/passwd"
    user_data = cmdexor.run_cmd(cmd)

    return user_data
