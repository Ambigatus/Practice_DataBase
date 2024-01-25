import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('movie_db.db')

# Making request to table "movie_dataset" and send data to interface "cursor"
cursor = conn.cursor()

# Send the request to get "ratings" from the database
query = """
    SELECT rating
    FROM movie_dataset
    WHERE rating != 'No Data'
"""

# Using Pandas to create Data Frame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Convert data to numeric, to prevent errors
df['rating'] = pd.to_numeric(df['rating'])

# Plot the "bar" chart
plt.figure(figsize=(10, 6))
df['rating'].value_counts().sort_index().plot(kind='bar', color='skyblue')

# Add information about data
plt.xlabel('Rating')
plt.ylabel('Number of Movies')
# Customize title
title_font = {'fontsize': 18, 'fontweight': 'bold', 'color': 'darkblue'}
plt.title('Distribution of Movie Ratings in 2023', fontdict=title_font)

# Add an annotation to chart, where this data was found
source_annotation = 'Data Source: IMDb, 2023'
plt.annotate(source_annotation, xy=(1, -0.12), xycoords='axes fraction', ha='right', fontsize=7, color='gray')

# Show visual
plt.show()
