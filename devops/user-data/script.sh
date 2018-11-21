#!/bin/bash -ex

source $(dirname $0)/common.sh

#------------------------#
# Install Search Service #
#------------------------#

INSTALL_DIR=/opt/geopython

# Setup the install directory and pull down the code
if [[ -d ${INSTALL_DIR} ]]; then rm -rf ${INSTALL_DIR}; fi
git clone https://github.com/thinkWhere/geopython17.git ${INSTALL_DIR}
cd ${INSTALL_DIR}
virtualenv-3 -p python3 env
source env/bin/activate
pip install -r ${INSTALL_DIR}/requirements.txt
pip install gunicorn
mkdir -p ${INSTALL_DIR}/instance

# Set permissions
groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask
chown -R flask:flaskgroup ${INSTALL_DIR}

# Exit virtualenv
deactivate

# Configure SystemD service and start
cp /vagrant/devops/systemd/geopython.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable geopython.service
systemctl restart geopython.service
systemctl status geopython

# Setup the firewall
yum install -y firewalld
systemctl enable firewalld
systemctl start firewalld
firewall-cmd --zone=public --permanent --add-port=5000/tcp
firewall-cmd --reload
