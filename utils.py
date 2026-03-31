def show_genres(movies):
    all_genres = set()

    for genres in movies["genres"]:
        for g in genres:
            all_genres.add(g)

    print("\nAvailable genres:")
    for genre in sorted(all_genres):
        print("-", genre)