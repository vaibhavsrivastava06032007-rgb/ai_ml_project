from data_loader import load_and_clean_data
from recommender import recommend_by_genre
from utils import show_genres

def main():
    print("Movie Recommender System")

    movies = load_and_clean_data("movies.csv")

    show_genres(movies)

    while True:
        choice = input("\nEnter a genre (or 'exit'): ").lower()

        if choice == "exit":
            print("Goodbye")
            break

        movie_list, suggestion = recommend_by_genre(movies, choice)

        if movie_list:
            print("\nMovies you can watch:")
            for movie in movie_list[:10]:  # show first 10 only
                print("-", movie)

            print("Suggested for you:", suggestion)
        else:
            print("No movies found for this genre")

if __name__ == "__main__":
    main()