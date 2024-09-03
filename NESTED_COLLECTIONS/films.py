movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama","Music"],
        "rating": 8.0
    }
]

# #q1total_number_of_movies
# total_num_of_movies=len(movies)
# print(total_num_of_movies)


# #q2movies with genre drama
# movies_with_DRAMA=[mov.get("title")for mov in movies if "Drama" in mov.get("genres")]
# print(movies_with_DRAMA)


# #q3 latest movie
# def get_year(mov):
#     return mov.get("year")
# latest_movie=max(movies,key=get_year)
# movie_filter=[mov.get("title")for mov in movies if mov.get("year")==latest_movie.get("year")]
# print(movie_filter)



# #q4 top movie with highest rating
# def get_rating(mov):
#     return mov.get("rating")
# top_rating=max(movies,key=get_rating)
# rating_filter=[mov.get("title")for mov in movies if mov.get("rating")==top_rating.get("rating")]
# print(rating_filter)


# #q5 movies with language malayalam
# malayalam_movies=[mov.get("title")for mov in movies if "Malayalam" in mov.get("language")]
# print(malayalam_movies)


# #q6 movies released after 2016
# movie_filter=[mov.get("title")for mov in movies if mov.get("year")>2016]
# print(movie_filter)


# #q7 movies with lowest ratings
# def get_ratings(mov):
#     return mov.get("rating")
# lowest_rating=min(movies,key=get_ratings)
# movie_filter=[mov.get("title")for mov in movies if mov.get("rating")==lowest_rating.get("rating")]
# print(movie_filter)


# #q8 malayalam movies with genre Action
# def get_genres(mov):
#     return mov.get("genres")
# action_genre=[mov.get("title")for mov in movies if "Action" in mov.get("genres")]
# print(action_genre)


#q9 movies released in same year
# movie_dictionary={}
# for mov in movies:
#     release_year=mov.get("year")
#     if release_year in movie_dictionary:
#         movie_dictionary.get(release_year).append(mov.get("title"))
#     else:
#         movie_dictionary[release_year]=[mov.get("title")]
# print(movie_dictionary)

            #or
# years=[mov.get("year")for mov in movies]
# print(years)

# years_count={y:years.count(y) for y in years }
# print(years_count)

# #q10 oldest movie
# def get_movies(mov):
#     return mov.get("year")
# oldest_movie=min(movies,key=get_movies)
# oldest_movie_name=[mov.get("title")for mov in movies if mov.get("year")==oldest_movie.get("year")]
# print(oldest_movie_name)


# #q11 movies name with generes either drama or comedy
# def get_genres(mov):
#     return mov.get("genres")
# DRAMA_or_COMEDY_genre=[mov.get("title")for mov in movies if "Drama" or "Comedy" in mov.get("genres")]
# print(DRAMA_or_COMEDY_genre)


# q12 print number of genres in movies withoy repeat
# genres=set()
# for mov in movies:
#     for g in mov.get("genres"):
#         genres.add(g)
# print(genres)
            #Or

# genres={g for mov in movies for g in mov.get("genres")}
# print(genres)


# #q13 genres_count
# all_genre=[g for mov in movies for g in mov.get("genres")]
# genres_count={g:all_genre.count(g) for g in all_genre}
# print(genres_count)


#q14 sort movie

# def get_title(mov):
#     return mov.get("title")
# sorted_movies=sorted(movies,key=get_title)
# sorted_movies_title=[mov.get("title")for mov in sorted_movies]
# print(sorted_movies_title)

            #or
sorted_movies=sorted(movies,key=lambda mov:mov.get("title"))
sorted_movies_title=[mov.get("title")for mov in sorted_movies]
print(sorted_movies_title)










