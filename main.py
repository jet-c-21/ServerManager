# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/3/22
"""
import server_manager as sm

from pprint import pp

if __name__ == '__main__':
    file_path = 'user_default_name.txt'
    user_json_sp = 'output/user_data.json'
    user_csv_sp = 'output/user_data.csv'

    # sm.create_user_json(file_path, user_json_sp)
    # sm.create_user_csv(file_path, user_csv_sp)
    #
    # df = sm.get_q_user_data_df(file_path)
    # print(df)

    x = sm.get_cmd_hist_df_by_user('Edward261')
    print(x)
