from flask import Flask, request, redirect, url_for
from flask import render_template
import movie as mv

app = Flask("Movie Database")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies')
def movies():
    movies = mv.load_movie_data()
    return render_template('movies.html', movies=movies)

@app.route('/movie/<movie_id>')
def movie_by_id(movie_id):
    movie = mv.load_movie_data_by_id(movie_id)
    return render_template('movie_details.html', movie=movie)

@app.route('/movie/create', methods=['GET', 'POST'])
def movie_create():
    if request.method == 'POST':
        movie_create_data = request.form.to_dict()
        mv.save_movie(movie_create_data)
        return redirect(url_for('movies'))
    return render_template('movie_create.html')

@app.route('/search')
def search():
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
