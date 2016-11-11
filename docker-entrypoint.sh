#!/bin/sh
sleep 45
#python manage.py collectstatic --noinput
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
