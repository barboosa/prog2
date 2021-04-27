import json

from flask import Flask
from flask import render_template

app = Flask("Hello World")

def load_movie_data():
    with open('./data/movies.json') as json_file:
        movies = json.load(json_file)
    return movies

@app.route('/')
def load_index():
    movies = load_movie_data()
    return render_template('index.html', movies=movies)


@app.route("/test")
def test():
    return "success"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
