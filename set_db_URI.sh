#!/bin/sh/

#Use passed SQLALCHEMY URI for db
echo $1 >> config.py
python db_create.py
python application.py
