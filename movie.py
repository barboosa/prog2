import json


def save(data):
    with open('./data/movies.json', 'w') as json_file:
        json_dump = json.dumps(data)
        json_file.write(json_dump)


def add_rating(movie_id, rating):
    movies = load_movie_data()
    for m in movies:
        if m['Id'] == int(movie_id):
            ratings = m["Ratings"]
            ratings.append(rating)
    save(movies)


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
    movie_create_data["Ratings"] = []
    movie_create_data["Watched"] = False
    movie_create_data["Watchlist"] = False
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


def get_watchlist():
    movies = load_movie_data()
    watchlist = []
    for m in movies:
        if m["Watchlist"]:
            for m in movies:
                watchlist.append(m)
    return watchlist


def set_watchlist(movie_id):
    movies = load_movie_data()
    for movie in movies:
        if movie["Id"] == int(movie_id):
            movie["Watchlist"] = not movie["Watchlist"]
            break
    save(movies)


def set_watched(movie_id):
    movies = load_movie_data()
    for movie in movies:
        if movie["Id"] == int(movie_id):
            movie["Watched"] = not movie["Watched"]
            break
    save(movies)


def delete_movie(movie_id):
    movies = load_movie_data()
    for i in range(len(movies)):
        if movies[i]["Id"] == int(movie_id):
            del movies[i]
            break
    save(movies)


