# Generate minimal sqlite database to support running django site
import sqlite3

# creates testing_db.sqlite3 which will 
# need to be renamed before inserting in django app
database_file = 'testing_db.sqlite3'

# Connecting to the database file
connection = sqlite3.connect(database_file)
db = connection.cursor()

# auth_group table
db.execute('CREATE TABLE "auth_group" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "name" varchar(80) NOT NULL UNIQUE)')

# auth_group_permissions table
db.execute('CREATE TABLE "auth_group_permissions" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "group_id" integer NOT NULL REFERENCES "auth_group" \
    ("id"), "permission_id" integer NOT NULL REFERENCES \
    "auth_permission" ("id"))')

# auth_permission table
db.execute('CREATE TABLE "auth_permission" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "content_type_id" integer NOT NULL REFERENCES \
    "django_content_type" ("id"), "codename" varchar(100) NOT NULL, \
    "name" varchar(255) NOT NULL)')

# auth_user table
db.execute('CREATE TABLE "auth_user" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "password" varchar(128) NOT NULL, "last_login" \
    datetime NULL, "is_superuser" bool NOT NULL, \
    "first_name" varchar(30) NOT NULL, "last_name" \
    varchar(30) NOT NULL, "email" varchar(254) NOT NULL, \
    "is_staff" bool NOT NULL, "is_active" bool NOT NULL, \
    "date_joined" datetime NOT NULL, "username" varchar(30) \
    NOT NULL UNIQUE)')
db.execute("INSERT INTO auth_user VALUES \
    (1,\
    'pbkdf2_sha256$24000$qyAg8Jbmv7Yb$u2Vpc9oKrNbkd/j/N3oRa3p9pZpYTJWYsDK6HoRDAfU=',\
    '2016-05-01', 1, '', '', 'tycobass@gmail.com', 1, 1, \
    '2016-05-01', 'eric')")

# auth_user_groups table
db.execute('CREATE TABLE "auth_user_groups" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "user_id" integer NOT NULL REFERENCES "auth_user" \
    ("id"), "group_id" integer NOT NULL REFERENCES "auth_group" \
    ("id"))')

# auth_user_user_permissions table
db.execute('CREATE TABLE "auth_user_user_permissions" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "user_id" integer NOT NULL REFERENCES "auth_user" \
    ("id"), "permission_id" integer NOT NULL REFERENCES \
    "auth_permission" ("id"))')

# django_admin_log table
db.execute('CREATE TABLE "django_admin_log" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "object_id" text NULL, "object_repr" varchar(200) \
    NOT NULL, "action_flag" smallint unsigned NOT NULL, \
    "change_message" text NOT NULL, "content_type_id" \
    integer NULL REFERENCES "django_content_type" ("id"), \
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), \
    "action_time" datetime NOT NULL)')

# django_content_type table
db.execute('CREATE TABLE "django_content_type" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL)')

# django_migrations table
db.execute('CREATE TABLE "django_migrations" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, \
    "applied" datetime NOT NULL)')

# django_session table
db.execute('CREATE TABLE "django_session" \
    ("session_key" varchar(40) NOT NULL PRIMARY KEY, \
    "session_data" text NOT NULL, "expire_date" datetime NOT NULL)')

# myblog_category table
db.execute('CREATE TABLE "myblog_category" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "name" varchar(128) NOT NULL, "description" text NOT NULL)')

# myblog_category_posts table
db.execute('CREATE TABLE "myblog_category_posts" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "category_id" integer NOT NULL REFERENCES \
    "myblog_category" ("id"), "post_id" integer NOT NULL REFERENCES \
    "myblog_post" ("id"))')

# myblog_post table
db.execute('CREATE TABLE "myblog_post" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "title" varchar(128) NOT NULL, "text" text NOT NULL, \
    "created_date" datetime NOT NULL, \
    "modified_date" datetime NOT NULL, "published_date" datetime NULL, \
    "author_id" integer NOT NULL REFERENCES "auth_user" ("id"))')

# sqlite_sequence(name,seq) table
#####db.execute('CREATE TABLE sqlite_sequence(name,seq)')

# userprofiles_profile table
db.execute('CREATE TABLE "userprofiles_profile" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "company" varchar(128) NOT NULL, \
    "user_id" integer NOT NULL UNIQUE REFERENCES \
    "auth_user" ("id"), "user_type_id" integer NULL REFERENCES \
    "userprofiles_usertype" ("id"))')

# userprofiles_project table
db.execute('CREATE TABLE "userprofiles_project" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "project" varchar(128) NOT NULL, \
    "project_slug" varchar(50) NOT NULL, \
    "address" varchar(128) NOT NULL, \
    "profile_id" integer NOT NULL REFERENCES \
    "userprofiles_profile" ("id"), \
    "project_type_id" integer NULL REFERENCES \
    "userprofiles_projecttype" ("id"))')

# userprofiles_project table
db.execute('CREATE TABLE "userprofiles_projecttype" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "project_type" varchar(128) NOT NULL)')
db.execute("INSERT INTO userprofiles_projecttype VALUES \
    (1,'ReModel')")
db.execute("INSERT INTO userprofiles_projecttype VALUES \
    (2,'New Construction')")

# userprofiles_usertype table
db.execute('CREATE TABLE "userprofiles_usertype" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "user_type" varchar(128) NOT NULL)')
db.execute("INSERT INTO userprofiles_usertype VALUES \
    (1,'Contractor')")
db.execute("INSERT INTO userprofiles_usertype VALUES \
    (2,'Home Owner')")

# wasteprocessors_materialtype table
db.execute('CREATE TABLE "wasteprocessors_materialtype" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "material_type" varchar(128) NOT NULL, \
    "description" text NOT NULL, \
    "special_considerations" text NOT NULL, \
    "material_slug" varchar(50) NOT NULL)')
db.execute("INSERT INTO wasteprocessors_materialtype VALUES \
    (1,'Wood', 'None', 'None', '')")
db.execute("INSERT INTO wasteprocessors_materialtype VALUES \
    (2,'Hardware', 'None', 'None', '')")

# wasteprocessors_waste table
db.execute('CREATE TABLE "wasteprocessors_waste" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "waste_type_id" integer NOT NULL REFERENCES \
    "wasteprocessors_wastetype" ("id"), \
    "material_type_id" integer NULL REFERENCES \
    "wasteprocessors_materialtype" ("id"), \
    "project_id" integer NOT NULL REFERENCES \
    "userprofiles_project" ("id"))')

# wasteprocessors_wasteprocessor table
db.execute('CREATE TABLE "wasteprocessors_wasteprocessor" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "company" varchar(128) NOT NULL, \
    "description" text NOT NULL, "phone" varchar(15) NOT NULL, \
    "email" varchar(254) NOT NULL, "address" varchar(128) NOT NULL, \
    "will_pick_up" bool NOT NULL, "will_purchase" bool NOT NULL, \
    "accepts_donations" bool NOT NULL, "accepts_salvage" bool NULL, \
    "accepts_scrap" bool NULL, "accepts_surplus" bool NULL, \
    "business_hours" text NOT NULL, "paid_service" bool NOT NULL, \
    "website" varchar(200) NOT NULL)')
db.execute("INSERT INTO wasteprocessors_wasteprocessor VALUES \
    (1,'Ballard Reuse', 'None', '206-297-9119', \
    'store@ballardreuse.com', '1440 NW 52nd St Seattle, WA', \
    1, 1, 1, NULL, NULL, NULL, '', 0, 'http://ballardreuse.com')")

# wasteprocessors_wasteprocessor_materials_accepted table
db.execute('CREATE TABLE \
    "wasteprocessors_wasteprocessor_materials_accepted" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "wasteprocessor_id" integer NOT NULL REFERENCES \
    "wasteprocessors_wasteprocessor" ("id"), \
    "materialtype_id" integer NOT NULL REFERENCES \
    "wasteprocessors_materialtype" ("id"))')
db.execute("INSERT INTO \
    wasteprocessors_wasteprocessor_materials_accepted VALUES \
    (1, 1, 1)")

# wasteprocessors_wastetype table
db.execute('CREATE TABLE "wasteprocessors_wastetype" \
    ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
    "waste_type" varchar(128) NOT NULL)')
db.execute("INSERT INTO wasteprocessors_wastetype VALUES \
    (1, 'Salvage')")
db.execute("INSERT INTO wasteprocessors_wastetype VALUES \
    (2, 'Scrap')")

# Committing changes
#connection.commit()



# Commit changes/close
connection.commit()
connection.close()