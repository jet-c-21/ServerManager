# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 3/17/22
"""
import subprocess

sp = subprocess.Popen('pwd', shell=False, universal_newlines=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o, e = sp.communicate()
print(e.splitlines())

sp.communicate('cd ..')

o, e = sp.communicate('pwd')
print(e.splitlines())