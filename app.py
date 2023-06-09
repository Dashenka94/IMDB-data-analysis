from flask import Flask, render_template
import pandas as pd
from data_for_movies import movies_over_time, directors, genres, high_rated_stars, genres_over_time, Votes_over_time
import numpy as np


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home_page.html')


@app.route('/movies')
def movies():
    df = movies_over_time.to_html()
    return render_template('index.html', table=df, title='IMDb rating over time', image = 'movies.png')

  
@app.route('/top_directors')
def top_directors():
    df = directors.to_html()
    return render_template('index.html', table=df, title='Top 10 directors', image = 'dir.png')


@app.route('/top_genres')
def top_genres():
    df = genres.to_html()
    return render_template('index.html', table=df, title='Top genres according to the rating', image = 'genres.png')




@app.route('/rated_stars')
def rated_stars():
    df = high_rated_stars.to_html()
    return render_template('index.html', table=df, title='High rated stars', image = 'stars.png')




@app.route('/genres_time')
def genres_per_time():
    df = genres_over_time.to_html()
    return render_template('index.html', table=df, title='Evolving of genres over time',  image = 'genres_time.png')



@app.route('/num_of_votes')
def num_of_votes():
    df = Votes_over_time.to_html()
    return render_template('index.html', table=df, title='Number of votes 1990 - 2020', image = 'votes.png')




if __name__ == '__main__':
    app.run(debug=True)