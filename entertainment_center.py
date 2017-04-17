import fresh_tomatoes
import media

# Defines attributes of the movie instances
delicatessen = media.Movie("Delicatessen",
                           "An apartment where the tenants are cannibals.",
                           "https://upload.wikimedia.org/wikipedia/en/0/04/Delicatessen2.jpg",
                           "https://www.youtube.com/watch?v=iYo_SkERMNI",
                           "(1991)")

amelie = media.Movie("Amelie",
                     "A woman brings magic to the people in her town.",
                     "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",
                     "https://www.youtube.com/watch?v=HUECWi5pX7o",
                     "(2001)")

city_of_lost_children = media.Movie("City of Lost Children",
                                    "A man tries to find his brother on an island where dreams are stolen.",
                                    "https://upload.wikimedia.org/wikipedia/en/4/40/City_of_lost_children_french_movie_poster.jpg",
                                    "https://www.youtube.com/watch?v=CNYG9cXTSds",
                                    "(1995)")

micmacs = media.Movie("Micmacs",
                      "Misfit group brings down arms dealers. With style.",
                      "https://upload.wikimedia.org/wikipedia/en/7/75/Micmacs_%C3%A0_tire-larigot.jpg",
                      "https://www.youtube.com/watch?v=TjKW0tG7I8s",
                      "(2009)")

t_s_spivet = media.Movie("The Young and Prodigious T.S. Spivet",
                         "A boy genius obsessed with perpetual motion.",
                         "https://upload.wikimedia.org/wikipedia/en/c/cc/The_Young_and_Prodigious_TS_Spivet_poster.jpg",
                         "https://www.youtube.com/watch?v=wjOYX_a8GXw",
                         "(2013)")

long_engagement = media.Movie("A Very Long Engagement",
                              "A young woman never gives up hope that her fiance will return from the war.",
                              "https://upload.wikimedia.org/wikipedia/en/7/76/A_Very_Long_Engagement_movie.jpg",
                              "https://www.youtube.com/watch?v=BNx2iuOGVVI",
                              "(2004)")

# Creates list of movies for fresh_tomatoes file to use as an argument
movies = [delicatessen, city_of_lost_children, amelie, long_engagement, micmacs, t_s_spivet]

fresh_tomatoes.open_movies_page(movies)
