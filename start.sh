#!/bin/bash 
gunicorn -c config.py  app:app

