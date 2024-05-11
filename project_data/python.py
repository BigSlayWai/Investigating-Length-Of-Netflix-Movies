# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding

# 1. Loading the data
netflix_df = pd.read_csv('netflix_data.csv')

# 2. Removing TV Shows from data and storing as netflix_subset
netflix_subset = netflix_df[netflix_df['type'] != 'TV Show']

# 3. Subsetting the columns of the new dataframe and saving this into a new DataFrame called netflix_movies
keep_columns = ['title', 'country', 'genre', 'release_year', 'duration']
netflix_movies = netflix_subset[keep_columns]

# 4. Flitering netflix_movies for movies < 60 minutes and storing this into short_movies
short_movies = netflix_movies[netflix_movies['duration'] < 60]

#5. Color coding movie genres by using a for loop and if/elif statements 
colors = []
for label, row in netflix_movies.iterrows():
    if row['genre'] == 'Children':
        colors.append('pink')
    elif row['genre'] == 'Documentaries':
        colors.append('black')
    elif row['genre'] == 'Stand-Up':
        colors.append('red')
    else:
        colors.append('green')

# 6. Initializing a new figure
fig = plt.figure(figsize = (14,10))
plt.scatter(netflix_movies.release_year, netflix_movies.duration, c = colors)

# 6. Adding labels and title
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie Duration by Year of Release')

# 6. Displaying the plot
plt.show()

# 7. Answering the question "Are we certain that movies are getting shorter?"
answer = "no"
