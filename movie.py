import json


def save(data):
    with open('./data/movies.json', 'w') as json_file:
        json_dump = json.dumps(data)
        json_file.write(json_dump)


def load_movie_data():
    try:
        with open('./data/movies.json') as json_file:
            movies = json.load(json_file)
    except:
        movies = []
    return movies


def load_movie_data_by_id(movie_id):
    movie = {}
    movies = load_movie_data()
    for m in movies:
        if m['Id'] == int(movie_id):
            movie = m
            break
    return movie


def save_movie(movie_create_data):
    movies = load_movie_data()
    new_id = len(movies) + 1
    movie_create_data["Id"] = new_id
    movies.append(movie_create_data)
    save(movies)


def search_movie(search_inputs):
    movies = load_movie_data()
    filtered_movies = []
    for key, value in search_inputs.items():
        if search_inputs[key]:
            for m in movies:
                if value in m[key]:
                    filtered_movies.append(m)
    return filtered_movies
