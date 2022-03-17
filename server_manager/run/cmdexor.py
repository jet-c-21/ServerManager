# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 3/16/22
"""
import subprocess
from typing import Union

'''
All the method for executing the commands in this file should be done in the server environment (locally)
'''


# >>>>>>>>>>>> Protect Members  >>>>>>>>>>>>
def _run_cmd(cmd: str) -> str:
    """
    run command directly and return raw text in one line
    :param cmd:
    :return:
    """
    return subprocess.check_output(cmd,
                                   stderr=subprocess.STDOUT,
                                   shell=True).decode('utf-8').strip()


def _run_cmd_by_open_proc(cmd: str) -> Union[str, None]:
    p = subprocess.Popen(cmd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)
    proc_out, proc_error = p.communicate()

    if proc_error:
        proc_error = proc_error.decode('utf-8').strip()
        msg = f"Process Error: {proc_error}"
        print(msg)
        return

    if proc_out:
        proc_out = proc_out.decode('utf-8').strip()

    return proc_out


# <<<<<<<<<<<< Protect Members  <<<<<<<<<<<<

def run_cmd(cmd: str) -> list:
    """
    run command and return parsed string as list
    :param cmd:
    :return:
    """
    return _run_cmd(cmd).split('\n')


def run_cmd_popen(cmd: str) -> list:
    return _run_cmd_by_open_proc(cmd).split('\n')
