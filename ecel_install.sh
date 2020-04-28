#!/bin/bash

# Script is used to install ECEL collectors on guest
# machine for AMED scenario analysis

# Needs to have chmod 755 ecel_install
# remember to sudo su command (Vagrant does this by default)

apt-get update
sleep 0.3

apt install -y net-tools
sleep 0.3

apt-get install -y gcc make curl python-pip python3-pip git expect 
sleep 0.3

pip3 install pymongo dnspython python-magic
sleep 0.3

pip install pymongo dnspython python-magic
sleep 0.3

apt-get install -y python3-pyqt5
sleep 0.3

git clone https://github.com/bwrobertson/AMEDPracticumSP20.git
sleep 0.3

cd AMEDPracticumSP20
sleep 0.3

git clone https://github.com/kevinHonsaker01/ecel.git
sleep 0.3

cd ecel
sleep 0.3

chown $HOSTNAME:$HOSTNAME -R ~/AMEDPracticumSP20
sleep 0.3

echo ECEL_HOME="\"${PWD}\"" >> /etc/environment
sleep 0.3

source /etc/environment
sleep 0.3

chown root:root standalone.sh
sleep 0.3

chmod 4755 standalone.sh
sleep 0.3

chmod 755 script.exp
sleep 0.3

mkdir /root/.config
sleep 0.3

mkdir /root/.config/autostart
sleep 0.3

./script.exp 
sleep 0.3

# to run collectors ./collectors (inside the ecel folder; exports data to Ben's DB)
# Need an interface to deliver the DB info user wants as their DB
# Possible way is to ask for this information at the VM install level and pass to 
# the Vagrantfile
