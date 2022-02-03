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