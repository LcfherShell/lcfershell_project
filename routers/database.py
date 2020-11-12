import sys
import os
import requests
from helper.tirtiparty.CtrlFSc import DbName

lists = ['mysql', 'postgress', 'sqlite', 'microsoft db', 'mongodb']
database = "sqlite:///myapp.sqlite3"

print(' * Database Status: Connect to '+DbName(database, lists))

