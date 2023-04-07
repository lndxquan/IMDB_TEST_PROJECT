import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('IMDB_Movie.csv')

# Task 1: Classify by country and count the number of Titles
country_count = df.groupby('Country')['Title'].count()
plt.pie(country_count, labels=country_count.index, autopct='%1.1f%%')
plt.title('Movies by Country')
plt.show()

# Task 2: Sort by actor and count the average score of all movies under the actor's name
actor_avg_score = df.groupby('Lead Actor')['IMDb_Rating'].mean().sort_values(ascending=False)

# Get the list of actors with a score over 8
top_actors = actor_avg_score[actor_avg_score > 8].index.tolist()

# Print the list of top actors
print('Top Actors with an Average Score above 8:')
print(top_actors)

# Task 3: Design an interaction to allow the user to enter the name of an actor and get the names of all movies under that actor's name
while True:
    actor = input('Enter the name of an actor or type "exit" to quit: ')
    if actor == 'exit':
        break
    movies = df.loc[df['Lead Actor'] == actor, ['Title', 'IMDb_Rating']]
    if movies.empty:
        print('No movies found for', actor)
    else:
        print('\nMovies under', actor, ':')
        print(movies)
