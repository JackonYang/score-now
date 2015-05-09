#!/bin/bash

rm -f db.sqlite3
python manage.py syncdb --noinput
python manage.py createsuperuser --username=jackon --email=jiekunyang@gmail.com

rm -rf media
cp -R init_data media
