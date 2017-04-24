#!/bin/sh/

#Use local SQLALCHEMY URI for db
echo "SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'" >> config.py
python db_create.py
python application.py
