#!/bin/bash

# Script is used to install ECEL collectors on guest
# machine for AMED scenario analysis

# Needs to have chmod 755 ecel_install
# remember to sudo su command (Vagrant does this by default)

apt-get update
apt install net-tools
apt-get install -y gcc make curl python-pip python3-pip git expect
pip3 install pymongo dnspython python-magic
pip install pymongo dnspython python-magic
apt-get install -y python3-pyqt5
git clone https://github.com/bwrobertson/AMEDPracticumSP20.git
cd AMEDPracticumSP20
git clone https://github.com/kevinHonsaker01/ecel.git
cd ecel
chown $HOSTNAME:$HOSTNAME -R ~/AMEDPracticumSP20
echo ECEL_HOME="\"${PWD}\"" >> /etc/environment
source /etc/environment

chown root:root collectors.sh
chmod 4755 collectors.sh
chmod 755 script.exp
mkdir /root/.config
mkdir /root/.config/autostart
./script.exp 

# to run collectors ./collectors (inside the ecel folder; exports data to Ben's DB)
# Need an interface to deliver the DB info user wants as their DB
# Possible way is to ask for this information at the VM install level and pass to 
# the Vagrantfile
