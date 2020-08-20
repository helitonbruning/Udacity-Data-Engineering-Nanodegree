# Summary of project
A music streaming startup, Sparkify, has grown their user base and song database even more and want to move their data warehouse to a data lake. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

# Project Description
In this project, you'll apply what you've learned on Spark and data lakes to build an ETL pipeline for a data lake hosted on S3. To complete the project, you will need to load data from S3, process the data into analytics tables using Spark, and load them back into S3. You'll deploy this Spark process on a cluster using AWS.

# Project Datasets
Song Data Path --> s3://udacity-dend/song_data Log Data Path --> s3://udacity-dend/log_data Log Data JSON Path --> s3://udacity-dend/log_json_path.json

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
