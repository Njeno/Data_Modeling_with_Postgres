# REVIEW

#start_time timestamp not null



# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""create table songplays(
                            song_play_id SERIAL, 
                            start_time timestamp NOT NULL, 
                            user_id int NOT NULL,
                            level varchar, 
                            song_id varchar, 
                            artist_id varchar,
                            session_id int NOT NULL,
                            location varchar,
                            user_agent varchar,
                            primary key(song_play_id)
                            );""")

user_table_create = ("""create table users(
                        user_id int, 
                        first_name varchar, 
                        last_name varchar,
                        gender varchar,
                        level varchar,
                        primary key(user_id)
                        );""")

song_table_create = ("""create table songs(
                        song_id varchar, 
                        title varchar, 
                        artist_id varchar, 
                        year int, 
                        duration float,
                        primary key(song_id)
                        );""")

artist_table_create = ("""create table artists(
                          artist_id varchar, 
                          name varchar, location varchar, 
                          latitude numeric,
                          longtitude numeric,
                          primary key(artist_id)
                          );""")

time_table_create = ("""create table time(
                        start_time timestamp, 
                        hour int, 
                        day int, 
                        week int, 
                        month int,
                        year int, 
                        weekday int,
                        primary key(start_time)
                        );""")


# INSERT RECORDS

songplay_table_insert = ("""insert into songplays(start_time , user_id ,level, song_id, artist_id, session_id, location, user_agent) 
                                                  values(%s,%s,%s,%s,%s,%s,%s,%s) 
                                                  ON CONFLICT (song_play_id) DO NOTHING
                                                  ;""")

user_table_insert = ("""insert into  users(user_id, first_name, last_name, gender, level) 
                                           values(%s,%s,%s,%s,%s) 
                                           ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level
                                           ;""")

song_table_insert = ("""
                        INSERT INTO songs (
                            song_id,
                            title,
                            artist_id,
                            year,
                            duration)
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""insert into artists(artist_id, name, location, latitude, longtitude) 
                                      values(%s,%s,%s,%s,%s) 
                                      ON CONFLICT (artist_id) DO NOTHING
                                      ;""")

time_table_insert = ("""insert into time(start_time, hour, day, week, month, year, weekday) 
                                    values(%s,%s,%s,%s,%s,%s,%s) 
                                    ON CONFLICT (start_time) DO NOTHING
                                    ;""")

# FIND SONGS

song_select = ("""select song_id,artists.artist_id from songs 
                  join artists on artists.artist_id = songs.artist_id 
                  where title = %s and artists.name = %s and duration = %s""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]