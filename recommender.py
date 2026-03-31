import random

def recommend_by_genre(movies, genre):
    genre = genre.lower()

    # Filter movies where genre exists in list
    filtered = movies[movies["genres"].apply(lambda x: genre in x)]

    if not filtered.empty:
        movie_list = filtered["title"].tolist()
        suggestion = random.choice(movie_list)
        return movie_list, suggestion
    else:
        return [], None