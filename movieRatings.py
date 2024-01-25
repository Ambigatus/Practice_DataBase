import matplotlib.pyplot as plt
from matplotlib.patheffects import withStroke
import sqlite3

# Connecting to db
conn = sqlite3.connect('movie_db.db')

# Creating interface "cursor" for taking information from database by using SQL-commands
cursor = conn.cursor()

# Making request to table "movie_dataset" and send data to interface "cursor"
cursor.execute("SELECT rating FROM movie_dataset WHERE rating != 'No Data'")

# Variable "ratings" keep all chosen data
ratings = cursor.fetchall()

# Create the plot type "histogram" for showing data. First, we convert all data from "ratings"
# in float format, cuz some data can be in "string". Then, we're creating plot "hist", with
# data from "ratings", 10 columns and edge color for better visualization. After, we're adding
# labels and shows the plot.
if ratings:
    ratings = [float(rating[0]) for rating in ratings]
    plt.hist(ratings, bins=10, edgecolor='black')
    title_font = {'fontsize': 15, 'fontweight': 'bold', 'color': 'orange'}
    title_text = plt.title('Distribution of Movie Ratings, 2023', fontdict=title_font)
    # Here we're using function "set_path_effects" from "matplotlib path effects" to outline the text
    title_text.set_path_effects([withStroke(linewidth=3, foreground='black')])
    plt.xlabel('Rating')
    plt.ylabel('Movies Count')
    # Add an annotation to chart, where this data was found
    source_annotation = 'Data Source: IMDb, 2023'
    plt.annotate(source_annotation, xy=(1, -0.12), xycoords='axes fraction', ha='right', fontsize=7, color='gray')
    plt.show()
else:
    print('No Data')

# Closing connection to database
conn.close()

