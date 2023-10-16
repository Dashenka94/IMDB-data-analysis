from flask import Flask, render_template
import pandas as pd
from data_for_movies import movies_over_time, directors, genres, high_rated_stars, genres_over_time, Votes_over_time
import numpy as np


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home_page.html')


datasets = {
    'movies': (movies_over_time, 'IMDb rating over time', 'movies.png'),
    'top_directors': (directors, 'Top 10 directors', 'dir.png'),
}


@app.route('/<dataset>')
def return_data(dataset):
    df = datasets[dataset][0].to_html()
    title = datasets[dataset][1]
    image = datasets[dataset][2]
    return render_template('index.html', table=df, title=title, image = image)

if __name__ == '__main__':
    app.run(debug=True)