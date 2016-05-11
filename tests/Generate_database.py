import os
import glob
from path import path


# Cleanup the django deployment to remove migrations
django_project = path('../../reConstruct')
print ('\nCleaning up old migrations')
for i in django_project.walk():
    if i.isdir() and i.name == 'migrations':
            print ('- Deleting folder = ', i)
            i.remove()

# Move db.sqlite3(if it exists) out of the way
from datetime import datetime
print ('\nMoving db.sqlite3 file out of the way if necessary')
if os.path.isfile('../db.sqlite3'):
    date = datetime.now().time()
    date_string = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    os.rename('../db.sqlite3', '../db_orig_' \
        + date_string + '.sqlite3')
    print ('- db.sqlite3 was moved')
    print ('- sqlite3 files remaining - ', \
        glob.glob('../*.sqlite3'))
else:
    print ('- No existing db.sqlite3 to be moved')

# Generate new base database
print ('\nCreating a new "empty" sqlite3 database')
os.system("python ../manage.py flush")

# Add migrations based upon apps
print ('\nCreating migrations based upon app specifics')
apps = ['userprofiles', 'wasteprocessors']
for j in apps: 
    os.system("python ../manage.py makemigrations " + j)

# Perform migration
print ('\nPerforming migrations')
os.system("python ../manage.py migrate")

# Populate database
print ('\nPopulating database')
os.system("python ../manage.py loaddata db_test.json")
