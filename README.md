# ServerManager
A python base Linux Server Management Tool

## Environment
- conda
```
conda create --name sm python=3.8 -y
```
- Jupyter Kernel
```
pip install ipykernel
python -m ipykernel install --user --name sm --display-name "Server Manager"
```

## Command History
- zsh
```
sudo -S grep -e "$pattern" /home/*/.bash_history >! cmd_hist.txt
```

## Class of User
("nobody" is auto-ignored)
#### 1. User
The user that will show up in the login screen
#### 2. Service User
Class 1 + "root" user
#### 3. System User
The program that runs in the os.

## Track Env Variable of each User
```shell script
$SHELL
$HISTFILE
$HISTSIZE
$HISTFILESIZE
```
