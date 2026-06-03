# Recommendation Function

def recommend_movies(movie_name, top_n=5):

    if movie_name not in movie_genre_map:
        return "Movie not found"

    input_genres = movie_genre_map[movie_name]

    recommended_genres = set()

    for _, row in rules.iterrows():

        for genre in input_genres:

            if genre in row['antecedents']:
                recommended_genres.update(
                    row['consequents']
                )

    recommended_movies = []

    for _, row in movies_df.iterrows():

        if row['title'] != movie_name:

            if any(
                genre in recommended_genres
                for genre in row['listed_in']
            ):
                recommended_movies.append(
                    row['title']
                )

    return list(set(recommended_movies))[:top_n]))

movie_name = input(
    "Enter Movie Name: "
)

recommendations = recommend_movies(
    movie_name
)

print("\nRecommended Movies:\n")

for movie in recommendations:
    print(movie)
