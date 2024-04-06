#creation of SQLite database
import sqlite3

conn = sqlite3.connect('etl_project.db')
cursor = conn.cursor()

#creating tables (if they dont exist)
cursor.execute("CREATE TABLE IF NOT EXISTS artists_songs (artist_name text not null, songs text primary key)")
cursor.execute("CREATE TABLE IF NOT EXISTS songs (title text primary key, day integer, month integer, year integer, streams integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS lyrics (song text primary key, lyrics text not null)")
cursor.execute("CREATE TABLE IF NOT EXISTS charts (song text primary key, spotify integer, apple integer, deexer integer, shazam integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS concerts (artist_name text, event text primary key, location text, venue text)")

#extracting info from csv

#pulling data from API


conn.commit()
conn.close()