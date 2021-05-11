import json

from flask import Flask, request
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
def index():
    return render_template('index.html')

@app.route('/movies')
def movies():
    movies = load_movie_data()
    return render_template('movies.html', movies=movies)

@app.route('/movie/<movie_id>')
def movie_by_id(movie_id):
    movie = load_movie_data_by_id(movie_id)
    return render_template('movie_details.html', movie=movie)

@app.route('/movie/create', methods=['GET', 'POST'])
def movie_create():
    movies = load_movie_data()
    if request.method == 'POST':
        movie_create_data = request.form
        return render_template('movies.html', movies=movies)
    return render_template('movie_create.html')

@app.route('/search')
def search():
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
