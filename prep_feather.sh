#!/bin/bash
echo 'This will require super user privilages! ^C now to exit and run as sudo.'
sudo apt-get install python-pip python-virtualenv
pip install flask flask-sqlalchemy mailchimp
echo 'Environment Set Up'
echo 'For development, run ". venv/bin/activate" to enable virtual environment'
echo 'For production, set up wsgi via apache2'