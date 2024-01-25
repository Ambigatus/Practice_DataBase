import sqlite3
import csv

# Connecting to db
conn = sqlite3.connect("movie_db.db")

# Creating interface "cursor" for taking information from database by using SQL-commands
cursor = conn.cursor()

# Open file with data, create an object "reader" for correct reading .csv file. Then, creating
# list with data from file.
with open("imdb_movie_data_2023.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

    for row in data:
        id = None

        try:
            id = int(row[0])
        except ValueError:
            print("Invalid value for 'id :", row[0])
            continue

        name = row[1]
        rating = "No Data" if row[2] == "NA" else float(row[2])
        votes = "No Data" if row[3] == "NA" else float(row[3])
        meta = "No Data" if row[4] == "NA" else int(row[4])
        genre = "No Data" if row[5] == "NA" else row[5]
        pg_rate = "No Data" if row[6] == "NA" else row[6]
        year = "No Data" if row[7] == "NA" else int(row[7])
        duration = "No Data" if row[8] == "NA" else row[8]
        cast = "No Data" if row[9] == "NA" else row[9]
        director = "No Data" if row[10] == "NA" else row[10]

        # Send all data inside database. Here we using placeholders "?" for preventing incorrect
        # data input
        cursor.execute("""
    INSERT INTO movie_dataset (name, rating, votes, meta, genre, pg_rate, year, duration, cast, director)
    VALUES (?,?,?,?,?,?,?,?,?,?)
    """, (name, rating, votes, meta, genre, pg_rate, year, duration, cast, director))

# Commit changes into database
conn.commit()

# Close connection
conn.close()
