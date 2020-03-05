#!/bin/sh
# This file sets up mongodb for python in your environment
# Author: Oyamo Brian oyamo.xyz@protonmail.com
# You are free to modify this file or submit complaints
echo "Setting up Mongo db for your environment"
echo "This installs the python module and the mongo server and starts the server"
echo "It is going to take Quite some Time"
python -m pip install pymongo
#python3 -m pip install pymongo
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc |  apt-key add -
apt-get install gnupg
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.2 main" |  tee /etc/apt/sources.list.d/mongodb-org-4.2.list
apt-get update
apt-get install -y mongodb-org
service mongod start
echo " Thank you for your Patience"
