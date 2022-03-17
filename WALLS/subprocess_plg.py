"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/26/21
"""
# coding: utf-8
import subprocess

# p1 = subprocess.run(['ls', '-la', 'dne'],
#                     capture_output=True,
#                     text=True,
#                     check=True)
# print(p1.stdout)

p1 = subprocess.run(['ls', '-la', 'dne'],
                    stderr=subprocess.DEVNULL)
print(p1.stdout)


subprocess.Popen

