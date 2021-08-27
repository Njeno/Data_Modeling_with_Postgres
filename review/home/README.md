# Data Modeling with Postgres

## Project Overview

### Introduction
A startup called Sparkify wants to analyze the data they collected on songs and user activity on their music streaming app. The analytics team is particularly interested in understanding what songs users are listening. Currently, there is no easy way for them to parse a huge number of JSON logs received through their streaming app

Sparkify want to ask a data engineer to program a Postgres database of tables that will optimize the Songplay analysis queries and make them available for the project. 
Your role now is to create a database schema and ETL pipeline for this analysis. We'll be able to test your database and ETL pipeline by running queries given to us by the analytics team from Sparkify and compare your results with their expected results.


### Project description
In this project we apply what we have learned about data modeling with Postgres and create an ETL pipeline with Python.
To complete the project, we need to define a fact and dimension table for a STAR schema for a specific analytical focus, write an ETL pipeline that imports the data from files in two local directories into these tables in Postgres using Python and SQL.

### Dataset:
#### Song Dataset
The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

#### Log Dataset
The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.

log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json
And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.


If you would like to look at the JSON data within log_data files, you will need to create a pandas dataframe to read the data. Remember to first import JSON and pandas libraries.

df = pd.read_json(filepath, lines=True)

For example, df = pd.read_json('data/log_data/2018/11/2018-11-01-events.json', lines=True) would read the data file 2018-11-01-events.json.


### Schema for Song Play Analysis
Using the song and log datasets, we'll be creating a STAR schema optimized for queries on song play analysis. This includes the following tables.


#### Fact Table

1. songplays - records in log data associated with song plays i.e. records with page NextSong
- songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent


#### Dimension Tables
2. users: users in the app
   user_id, first_name, last_name, gender, level
3. songs: songs in music database
   song_id, title, artist_id, year, duration
4. artists: artists in music database
   artist_id, name, location, lattitude, longitude
5. time: timestamps of records in songplays broken down into specific units
   start_time, hour, day, week, month, year, weekday


In addition to the data files, the project workspace includes six files:

1. test.ipynb displays the first few rows of each table to let you check your database.
2. create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
3. etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
4. etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
5. sql_queries.py contains all your sql queries, and is imported into the last three files above.
6. Readme.md


### Project Steps

1. Create Tables
- Create a STAR scheme tables for ETL pipeline 
- Write CREATE statements in sql_queries.py to create each table.
- Write DROP statements in sql_queries.py to drop each table if it exists.
- Run create_tables.py to create your database and tables.
- Run test.ipynb to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.


### Build ETL Processes
- Follow instructions in the etl.ipynb notebook to develop ETL processes for each table. 
- At the end of each table section, or at the end of the notebook, run test.ipynb to confirm that records were successfully inserted into each table. 


### Build ETL Pipeline
- Use what you've completed in etl.ipynb to complete etl.py, where you'll process the entire datasets.  
- Run test.ipynb to confirm your records were successfully inserted into each table.
