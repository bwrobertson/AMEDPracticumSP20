#!/bin/bash

# Needs to have chmod 755 ecel_install
# remember to sudo su

kill -9 $(ps aux | grep -i apt | grep usr | cut -d" " -f7) # removes the lock on update
apt-get update
apt-get install -y gcc make curl python-pip python3-pip git expect
pip3 install pymongo dnspython
pip install pymongo dnspython
apt-get install python3-pyqt5
git clone https://github.com/kevinHonsaker01/ecel.git
cd ecel
echo ECEL_HOME="\"${PWD}\"" >> /etc/environment
source /etc/environment

chmod 755 collectors.sh
chmod 755 script.exp
./script.exp 

# to run collectors ./collectors (inside the ecel folder; exports data to Ben's DB)
