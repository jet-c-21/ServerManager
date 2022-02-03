# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/3/22
"""
import subprocess as sb
import json


def read_json(fp: str) -> dict:
    return json.load(open(fp, 'r', encoding='utf-8'))


def to_json(data, fp: str):
    json.dump(data, open(fp, 'w', encoding='utf-8'), indent=4, ensure_ascii=False)


def _run_cmd(cmd: str) -> str:
    """
    run command directly and return raw text in one line
    :param cmd:
    :return:
    """
    return sb.check_output(cmd,
                           stderr=sb.STDOUT,
                           shell=True).decode('utf-8').strip()


def run_cmd(cmd: str) -> list:
    """
    run command and return parsed string as list
    :param cmd:
    :return:
    """
    return _run_cmd(cmd).split('\n')
