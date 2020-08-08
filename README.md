# Summary of project
Startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project.

# How to run the python scripts
To create the database tables and run the ETL pipeline, you must run the following two files in the order that they are listed below

To create tables:
* python3 create_tables.py

To fill tables via ETL:
* python3 etl.py

# The purpose of this database
By using SQL and the star scheme, joins and aggregations, the data can be searched and summarized quickly and easily. By using a relational database.

![er](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/33760/1596767636/Song_ERD.png)

# Files in the repository
* [create_tables.py](\create_tables.py): Python script to perform SQL-Statements for (re-)creating database and tables
* [sql_queries.py](\sql_queries.py): Python script containing SQL-Statements used by create_tables.py and etl.py
* [etl.py](\etl.py): Python script to extract the needed information from Song and Log data inside the data folder and parsing/inserting them to the created database schema and tables
