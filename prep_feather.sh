#!/bin/bash
echo 'This will require super user privilages! ^C now to exit and run as sudo.'
sudo apt-get install python-pip python-virtualenv -y --force-yes
. venv/bin/activate
pip install flask flask-sqlalchemy mailchimp markdown
echo 'Environment Set Up'
