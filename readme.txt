Team: The Primary Keys
Members: Josh McKone, Ruiqi Zhao, Varun Apte

Welcome to the Primary Keys Flask Application
START:
After opening the project directory, please ensure that you install the following packages
Package            Version
------------------ -------
alembic            1.7.7
dnspython          2.2.1
email-validator    1.2.0
Flask              2.1.2
Flask-Admin        1.6.0
Flask-Login        0.6.0
Flask-Migrate      3.1.0
Flask-Session      0.4.0
Flask-SQLAlchemy   2.5.1
Flask-WTF          1.0.1
importlib-metadata 4.11.3
Jinja2             3.1.2
pip                21.1.2
PyMySQL            1.0.2
python-dotenv      0.20.0
setuptools         57.0.0
SQLAlchemy         1.4.36
Werkzeug           2.1.2
WTForms            3.0.1
-All of these packages are required to be included in order for the application to properly work.
-After installing these packages, make sure that your database has started.

STARTING AND USING THE APPLICATION:
-In order to start the application make sure you are in your virtual environment
and run the command "flask run"
-This will generate a link in the command line, click on this link.
-You will then login and be able to query the application with teams and years.
-After submitting a team and year the application will generate a list of tables. Each table is titled with a specific player
-Each table represents the number of games played in each position by the player for that year. 

ADMIN MODE:
-To login as an admin signout of your current account and sign in with
username: "Admin"
password: "ilovedatabase"
-Once logged in as the Admin you will be able to do all things a normal user 
can as well as accessing the admin page.

ACCESSING THE ADMIN PAGE:
-paste http://127.0.0.1:5000/admin to the link in the browser

USING THE ADMIN PAGE:
-Upon logging in as an admin you will find a new link in the upper left hand corner labeled Log, click on this link.
-You will then find 2 relevant tabs: Users and teams table
-If you click on the Users tab you will be able to see all the current Users, you can also add Users from this page.
-If you click on the teams Table you will find all of the queries made by users. 
-Each row in the teams table represents one query that is connected to one User.
-Each user can have multiple queries.
-The usert column represents the user that made the query.
-The Team Choose and Year Choose columns represent the team and year queried respectively


-------------------------------

Database Information:

Packages Used:
numpy
pymysql
pandas

New Hall of Fame data taken from:
https://www.baseball-reference.com/awards/hof.shtml

For full list of indexes added, see changes.sql

Additional changes made to database:
-All tables that previously had "ID" have had that column replaced with a more fitting column name to allow for Natural Joins easier
	I.E. allstarfull "ID" -> "as_ID"
	For the full list of Column changes, see changes.sql
-Added G_rf to appearances table
-Changed fieldingpost "f_WP" column to "f_TP" to match the data from the csv file
-Dropped the "f_ZR" column in fieldingpost table to match the data from the csv file
-Dropped awards table due to missing data, and missing csv files
-Dropped awardsshare table due to missing data, and missing csv files
-Dropped school table due to missing data, and missing csv files
-Dropped salary table due to missing data, and missing csv files


Additional Notes:
changes.sql - Contains all of the individual sql changes for an existing database. Schema.sql is the one intended for use.