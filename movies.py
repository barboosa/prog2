import json

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


def save_movie(movie_create_data):
    return None