import pandas as pd

def load_and_clean_data(file_path):
    movies = pd.read_csv(file_path)

    # Convert genres to lowercase
    movies["genres"] = movies["genres"].str.lower()

    # Convert "Romance Drama" → ["romance", "drama"]
    movies["genres"] = movies["genres"].str.split()

    return movies