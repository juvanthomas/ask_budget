#!/bin/bash
sudo su
cd /var/lib/jenkins/workspace/budget
source venv/bin/activate
cd files
pip3 install -r requirments.txt
