import json


def load_movie_data():
    try:
        with open('./data/movies.json') as json_file:
            movies = json.load(json_file)
    except:
        movies = []
    return movies


def save(data):
    with open('./data/movies.json', 'w') as json_file:
        json_dump = json.dumps(data)
        json_file.write(json_dump)


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


def add_rating(movie_id, rating):
    movies = load_movie_data()
    for m in movies:
        if m['Id'] == int(movie_id):
            ratings = m["Ratings"]
            ratings.append(rating)
    save(movies)


def get_watchlist():
    movies = load_movie_data()
    watchlist = []
    for m in movies:
        if m["Watchlist"]:
            watchlist.append(m)
    return watchlist


def get_watched_movies():
    movies = load_movie_data()
    watched_movies = []
    for m in movies:
        if m["Watched"]:
            watched_movies.append(m)
    return watched_movies


def set_watchlist(movie_id):
    movies = load_movie_data()
    for m in movies:
        if m["Id"] == int(movie_id):
            m["Watchlist"] = not m["Watchlist"]
            break
    save(movies)


def set_watched(movie_id):
    movies = load_movie_data()
    for m in movies:
        if m["Id"] == int(movie_id):
            m["Watched"] = not m["Watched"]
            break
    save(movies)


def delete_movie(movie_id):
    movies = load_movie_data()
    # https://www.w3schools.com/python/python_lists_comprehension.asp (Comprehension anstatt for schleife mit append, alles was übereinstimmt mit if wird zur Liste hinzugefügt, Problem beim iterieren und gleichzeitigen löschen von liste)
    data = [m for m in movies if m["Id"] != int(movie_id)]
    save(data)


def get_movie_recommendation(genre):
    movies = load_movie_data()
    watchlist = get_watchlist()
    watched = get_watched_movies()

    if watchlist:
        recommended_list = watchlist
        if genre:
            recommended_list = [rl for rl in recommended_list if rl["Genre"] == genre]
    else:
        recommended_list = movies
        if genre:
            recommended_list = [rl for rl in recommended_list if genre and rl["Genre"] == genre]

    for w in watched:
        if w in recommended_list:
            recommended_list.remove(w)

    if recommended_list:
        if len(recommended_list) == 1:
            return recommended_list[0]["Id"]
        else:
            for rl in recommended_list:
                if rl["Ratings"]:
                    rating_total = 0
                    for r in rl["Ratings"]:
                        rating_total += float(r["Rating"])
                    rl["AverageRating"] = rating_total / len(rl["Ratings"])
                else:
                    rl["AverageRating"] = 0

            recommended_list = sorted(recommended_list, key=lambda k: k["AverageRating"], reverse=True)
            return recommended_list[0]["Id"]
    else:
        return []
