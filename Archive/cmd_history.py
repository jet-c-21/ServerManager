# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/3/22
"""
import pandas as pd
from tqdm import tqdm

from .ult import run_cmd_popen


def get_all_user_raw_cmd_hist_data_with_interaction() -> list:
    cmd = 'sudo -S grep -e \"$pattern\" /home/*/.bash_history'
    return run_cmd_popen(cmd)


def get_all_user_raw_cmd_hist_data(su_pwd: str) -> list:
    cmd = f"echo {su_pwd} | sudo -S grep -e \"$pattern\" /home/*/.bash_history"
    return run_cmd_popen(cmd)


def get_cmd_hist_df_by_user(su_pwd=None) -> pd.DataFrame:
    result = pd.DataFrame(columns=['CommandID', 'User', 'Command'])

    if su_pwd:
        raw_cmd_hist = get_all_user_raw_cmd_hist_data(su_pwd)
    else:
        raw_cmd_hist = get_all_user_raw_cmd_hist_data_with_interaction()

    raw_cmd_hist_df = pd.DataFrame(columns=['user', 'cmd'])
    for s in tqdm(raw_cmd_hist, desc='Collecting All Command History'):
        s: str
        token_ls = s.split('/.bash_history:')
        cmd = token_ls[-1]
        user = token_ls[0].split('/')[-1]
        record = [user, cmd]

        raw_cmd_hist_df.loc[len(raw_cmd_hist_df)] = record

    raw_cmd_hist_df_gb = raw_cmd_hist_df.groupby(['user'])
    for user, group in tqdm(raw_cmd_hist_df_gb, desc='Parsing'):
        group = group.reset_index(drop=True)
        group.index += 1
        for i, row in group.iterrows():
            cmd_id = f"{user}@{i}"
            cmd = row['cmd']
            record = [cmd_id, user, cmd]

            result.loc[len(result)] = record

    return result
