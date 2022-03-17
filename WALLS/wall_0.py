# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 3/17/22
"""
import os
import subprocess

p1 = subprocess.run('pwd', shell=True, capture_output=True, text=True)
print(p1.stdout)

subprocess.run('cd ..', shell=True, capture_output=True, text=True)

p1 = subprocess.run('pwd', shell=True, capture_output=True, text=True)
print(p1.stdout)

