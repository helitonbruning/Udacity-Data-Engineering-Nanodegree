# Summary of project
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

# Project Description
Application of Data warehouse and AWS to build an ETL Pipeline for a database hosted on Redshift Will need to load data from S3 to staging tables on Redshift and execute SQL Statements that create fact and dimension tables from these staging tables to create analytics

# Project Datasets
All datasets consists of log files in JSON format.
* Song Data Path --> s3://udacity-dend/song_data 
* Log Data Path --> s3://udacity-dend/log_data 
* Log Data JSON Path --> s3://udacity-dend/log_json_path.json

# Schema for Song Play Analysis
A Star Schema would be required for optimized queries on song play queries

> ### Fact Table
>
> **SONGPLAYS** - records in event data associated with song plays i.e. records with page NextSong
>
> * songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

> ### Dimension Tables
>
> **USERS** - users in the app
> * user_id, first_name, last_name, gender, level
>
> **SONGS** - songs in music database
> * song_id, title, artist_id, year, duration
>
> **ARTISTS** - artists in music database
> * artist_id, name, location, lattitude, longitude
>
> **TIME** - timestamps of records in **songplays** broken down into specific units
> * start_time, hour, day, week, month, year, weekday

# Project Template

Project Template include four files:

1. create_table.py is where you'll create your fact and dimension tables for the star schema in Redshift.

2. etl.py is where you'll load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.

3. sql_queries.py is where you'll define you SQL statements, which will be imported into the two other files above.

4. README.md is where you'll provide discussion on your process and decisions for this ETL pipeline.
