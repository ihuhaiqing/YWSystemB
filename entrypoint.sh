#!/bin/bash
cd /ywsystem
export ENV_FILE_YWSYSTEMB=YWSystemB/.prod

python -m pip install --upgrade pip
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple importlib-metadata==3.10.1
pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt

gunicorn YWSystemB.wsgi --bind=0.0.0.0:8000 --log-file logs/INFO.log --workers 8
