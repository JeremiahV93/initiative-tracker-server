#!/bin/bash


rm -rf initiativeTrackerApi/migrations
rm db.sqlite3
python manage.py makemigrations initiativeTrackerApi
python manage.py migrate
python manage.py loaddata users
python manage.py tokens
python manage.py loaddata campaigns
python manage.py loaddata encounters
python manage.py loaddata PCs
python manage.py loaddata monsters
python manage.py loaddata monster_pairs
python manage.py loaddata player_pair
