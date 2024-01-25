import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Connect to database
with sqlite3.connect('movie_db.db') as conn:
    # Choose all "genre" from the database
    query = "SELECT genre FROM movie_dataset WHERE genre != 'No Data'"
    # Split data, cuz some movies have more than 1 genre
    genres = [genre.split(', ') for (genre,) in conn.execute(query).fetchall()]

# Close connection to db
conn.close()

# Split data to get lists with same genres
flat_genres = [genre for sublist in genres for genre in sublist]

# Counting uniq genres
genre_counter = Counter(flat_genres)

# Create DF
df_genres = pd.DataFrame(list(genre_counter.items()), columns=['Genre', 'Movie Count'])

# Filter genres, cuz i didnt want to have a lot of small parts
threshold_percentage = 1
total_movies = df_genres['Movie Count'].sum()
df_genres_filtered = df_genres[df_genres['Movie Count'] / total_movies * 100 >= threshold_percentage]

# This is how we do things in the kitchen!
plt.figure(figsize=(12, 12))

# Customize text on pie
plt.pie(
    df_genres_filtered['Movie Count'],
    labels=df_genres_filtered['Genre'],
    autopct='%1.1f%%',
    startangle=140,
    textprops={'fontsize': 10, 'color': 'darkblue'},
    radius=1,
)

# Add a title and additional info, customize
title_font = {'fontsize': 18, 'fontweight': 'bold', 'color': 'darkblue'}
plt.title('Distribution of Movies by Genre, 2023', fontdict=title_font)
additional_info = f"Genres with less than {threshold_percentage}% representation are excluded."
plt.suptitle(additional_info, fontsize=10, color='gray', y=0.88)

# Add an annotation to chart, where this data was found
source_annotation = 'Data Source: IMDb, 2023'
plt.annotate(source_annotation, xy=(1, -0.12), xycoords='axes fraction', ha='right', fontsize=7, color='gray')

# Display the chart
plt.show()
