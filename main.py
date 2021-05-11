import json

from flask import Flask
from flask import render_template

app = Flask("Hello World")

def load_movie_data():
    with open('./data/movies.json') as json_file:
        movies = json.load(json_file)
    return movies

def load_movie_data_by_id(movie_id):
    with open('./data/movies.json') as json_file:
        movie = {}
        movies = json.load(json_file)
        for m in movies:
            if m['Id'] == int(movie_id):
                movie = m
            break
    return movie

@app.route('/')
def load_index():
    return render_template('index.html')

@app.route('/movies')
def load_movies():
    movies = load_movie_data()
    return render_template('movies.html', movies=movies)

@app.route('/movie/<movie_id>')
def load_movie_by_id(movie_id):
    movie = load_movie_data_by_id(movie_id)
    return render_template('movie_details.html', movie=movie)

@app.route('/search')
def load_search():
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
