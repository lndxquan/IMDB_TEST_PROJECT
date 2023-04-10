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
actor_avg_score = df.groupby('LeadActor')['IMDb_Rating'].mean().sort_values(ascending=False)

# Get the list of actors with a score over 8
top_actors = actor_avg_score[actor_avg_score > =8].index.tolist()

# Print the list of top actors
print('Top Actors with an Average Score above 8:')
print(top_actors)

# Task 3: Design an interaction 
while True:
    actor_name = input('Enter the name of an actor (or "quit" to exit): ')
    if actor_name.lower() == 'quit':
        break
    actor_movies = df[df['LeadActor'] == actor_name][['Title', 'IMDb_Rating']]
    if actor_movies.empty:
        print(f"No movies found for actor {actor_name}.")
    else:
        print(f"Movies for actor {actor_name}:")
        print(actor_movies)

# Allow the user to query all the information of the movie by inputting the name of the movie
while True:
    movie_title = input('Enter the name of a movie (or "quit" to exit): ')
    if movie_title.lower() == 'quit':
        break
    movie_info = df[df['Title'] == movie_title]
    if movie_info.empty:
        print(f"No information found for movie {movie_title}.")
    else:
        print(f"Information for movie {movie_title}:")
        print(movie_info)

# Allow the user to query all the movies under the name of a director
while True:
    director_name = input('Enter the name of a director (or "quit" to exit): ')
    if director_name.lower() == 'quit':
        break
    director_movies = df[df['DirectorName'] == director_name]
    if director_movies.empty:
        print(f"No movies found for director {director_name}.")
    else:
        print(f"Movies for director {director_name}:")
        print(director_movies)
