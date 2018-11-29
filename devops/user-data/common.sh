#!/bin/bash -e

# See if this is a noop
if [[ -f /root/common-user-data-complete ]]; then
    echo "Common code already complete. Skipping..."
else

# Add EPEL repo
yum --enablerepo=extras -y install epel-release
yum-config-manager --enable epel

# Update packages
yum upgrade -y

# Enable automatic updates
sudo yum -y install yum-cron
systemctl enable yum-cron
systemctl start yum-cron
cat >/etc/yum/yum-cron.conf <<EOL
[commands]
update_cmd = security
update_messages = yes
download_updates = yes
apply_updates = yes
random_sleep = 360

[emitters]
system_name = None
emit_via = stdio
output_width = 80

[email]
email_from = root@localhost
email_to = root
email_host = localhost

[groups]
group_list = None
group_package_types = mandatory, default

[base]
debuglevel = -2
mdpolicy = group:main
EOL

# Extra tools
yum install -y git htop vim tree ccze

# Install Python and pip
yum groupinstall -y 'development tools'
yum install python python34-devel python34-pip python34-virtualenv -y
pip3 install --upgrade pip

# Install and run Watchmaker
pip install watchmaker
export LC_ALL=en_US.utf8
export LANG=en_US.utf8
#watchmaker --no-reboot --env prod

# Set clean exit flag
if [[ $? -eq 0 ]]; then
    touch /root/common-user-data-complete
fi

fi
