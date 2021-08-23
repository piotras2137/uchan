#!/bin/bash

echo "updating uchan"

git fetch && git pull 

echo "creating database"

python manage.py migrate

echo "do you want to create super user?"

echo "starting serwer"

python manage.py runserver 