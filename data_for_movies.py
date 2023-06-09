import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


all_data = pd.read_csv('imdb_top_1000.csv')

all_data['Released_Year'].unique()
all_data = all_data[all_data['Released_Year'] != 'PG']
all_data['Released_Year'] = all_data['Released_Year'].astype(int)
all_data['decade'] = (all_data['Released_Year'] - 1900)// 10 * 10 + 1900
movies_over_time = pd.DataFrame(all_data.groupby('decade')['IMDB_Rating'].mean())
#figure = plt.figure(figsize=(6, 4))
plt.plot(movies_over_time.index, movies_over_time.values)
plt.xlabel('Decade')
plt.ylabel('Avg IMDB_Rating per decade')
plt.title('Rating of  Movies Over Time', fontsize = 18)
plt.grid(True)
plt.savefig('/users/dariatsymbal/Desktop/projects/Netflix/static/movies.png')
plt.tight_layout()



directors = all_data[['Director', 'IMDB_Rating', 'Series_Title']].groupby('Director').agg({'Series_Title': 'count', 'IMDB_Rating': 'mean'}).sort_values(by = 'Series_Title',  ascending=False)
directors = directors.rename(columns={'Series_Title': 'Movie_Count'})
directors = directors[directors['Movie_Count'] >= 3]
directors = directors.sort_values(by = 'IMDB_Rating', ascending = False)
plt.figure(figsize=(15,10))
plt.plot(directors.index[:10], directors['IMDB_Rating'][:10])
plt.xlabel('Director')
plt.ylabel('IMDB_Rating_AVG')
plt.title('Top 10 directors accoring to IMDB_Rating', fontsize = 18)
plt.grid(True)
plt.xticks(rotation=75)
plt.savefig('/users/dariatsymbal/Desktop/projects/Netflix/static/dir.png')





def fun(x):
    splitted = x.split(',')
    return [i.strip() for i in splitted]
all_data['Genre'] = all_data['Genre'].apply(fun)
all_data.explode('Genre')
genres = all_data[['Genre', 'IMDB_Rating']].explode('Genre').groupby('Genre').mean()
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(genres.index, genres.values)
plt.xlabel('Genre')
plt.ylabel('Average rating')
plt.title('Top genres according to the rating', fontsize = 18)
plt.grid(True)
plt.xticks(rotation=75)
plt.savefig('/users/dariatsymbal/Desktop/projects/Netflix/static/genres.png')









all_data['all_stars'] = all_data.apply(lambda row: [row['Star1'], row['Star2'], row['Star3'], row['Star4']], axis=1)
high_rated_stars = all_data[['all_stars', 'IMDB_Rating', 'Series_Title']].explode('all_stars').groupby('all_stars').agg({'IMDB_Rating': 'mean', 'Series_Title': 'count'}) 
high_rated_stars = high_rated_stars[high_rated_stars['Series_Title'] >= 3]
high_rated_stars = high_rated_stars.sort_values(by = 'IMDB_Rating', ascending = False)

fig, ax = plt.subplots(figsize=(8, 6))
plt.bar(high_rated_stars.index[:20], high_rated_stars['IMDB_Rating'][:20])
plt.xlabel('Star')
plt.ylabel('average IMDB_Rating')
plt.title('Highest rated stars (played in at least 3 movies)', fontsize = 18)
plt.ylim(8, 9.0)
plt.grid(True)
plt.xticks(rotation=75)
plt.savefig('/users/dariatsymbal/Desktop/projects/Netflix/static/stars.png'),



genres_over_time = all_data[['Genre', 'Released_Year', 'Series_Title']].explode('Genre').groupby(['Released_Year', 'Genre']).count()
pivot_table = genres_over_time.pivot_table(values='Series_Title', index='Released_Year', columns='Genre', aggfunc={'Series_Title': np.sum})
plt.figure(figsize=(12, 8))
plt.plot(pivot_table.index, pivot_table['Action'], label='Action')
plt.plot(pivot_table.index, pivot_table['Drama'], label='Drama')
plt.plot(pivot_table.index, pivot_table['Adventure'], label='Adventure')
plt.plot(pivot_table.index, pivot_table['Comedy'], label='Comedy')
plt.plot(pivot_table.index, pivot_table['Crime'], label='Crime')
plt.plot(pivot_table.index, pivot_table['Fantasy'], label='Fantasy')
plt.plot(pivot_table.index, pivot_table['Horror'], label='Horror')
plt.plot(pivot_table.index, pivot_table['Film-Noir'], label='Film-Noir')
plt.plot(pivot_table.index, pivot_table['Sci-Fi'], label='Sci-Fi')
plt.plot(pivot_table.index, pivot_table['Romance'], label='Romance')
plt.plot(pivot_table.index, pivot_table['Thriller'], label='Thriller')
plt.plot(pivot_table.index, pivot_table['War'], label='War')
plt.plot(pivot_table.index, pivot_table['Western'], label='Western')
plt.xlabel('Released Year')
plt.ylabel('Number of Movies')
plt.title('Evolving of Genres Over Time')
plt.ylim(0, 22)
plt.xlim(1960, 2020)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.savefig('/users/dariatsymbal/Desktop/projects/Netflix/static/genres_time.png')





Votes_over_time = all_data[['No_of_Votes', 'Released_Year']].groupby('Released_Year').mean()
fig, ax = plt.subplots(figsize=(8, 6))

plt.plot(Votes_over_time.index, Votes_over_time.values)
plt.xlabel('Released_Year')
plt.ylabel('No_of_Votes')
plt.title('Number of votes', fontsize = 18)
plt.grid(True)
plt.xlim(1930, 2020)
plt.xticks(rotation=75)
plt.tight_layout()
plt.savefig('/users/dariatsymbal/Desktop/projects/Netflix/static/votes.png')
