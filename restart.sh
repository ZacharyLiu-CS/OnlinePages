#!/bin/bash 
PROC_NAME="gunicorn"
echo "restarting service: OnlinePages"
pidvar=`ps x | grep "${PROC_NAME}" | grep -v "grep" | grep -v "bash" | awk '{print $1}'`
for i in $pidvar
do
	kill -9  $i
done
gunicorn -c config.py -b 0.0.0.0:18080 app:app

