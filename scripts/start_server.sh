#!/bin/bash
cd /home/ec2-user/python_app
pkill -f app.py || true
nohup python3 app/app.py > /home/ec2-user/python_app/app.log 2>&1 &
