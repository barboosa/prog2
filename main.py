from flask import Flask, request, redirect, url_for
from flask import render_template
import movie as mv

app = Flask("Movie Database")

@app.route('/')
def index():
    watchlist = mv.get_watchlist()
    return render_template('index.html', watchlist=watchlist)

@app.route('/movies')
def movies():
    movies = mv.load_movie_data()
    return render_template('movies.html', movies=movies)

@app.route('/movie/<movie_id>', methods=['GET', 'POST'])
def movie_by_id(movie_id):
    movie = mv.load_movie_data_by_id(movie_id)
    if request.method == 'POST':
        rating = request.form.to_dict()
        mv.add_rating(movie_id, rating)
        return render_template('movie_details.html', movie=movie)
    return render_template('movie_details.html', movie=movie)

@app.route('/movie/create', methods=['GET', 'POST'])
def movie_create():
    if request.method == 'POST':
        movie_create_data = request.form.to_dict()
        mv.save_movie(movie_create_data)
        return redirect(url_for('movies'))
    return render_template('movie_create.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_inputs = request.form.to_dict()
        movies = mv.search_movie(search_inputs)
        return render_template('movies.html', movies=movies)
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
