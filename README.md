# movie-site

## Introduction
This project creates a movie website which shows the movie title, release year, and movie trailer.

## Code Example
`class Movie():` in the media.py file defines the required information for instances of the class (`movie_title`, `movie_storyline`, `poster_image`, `trailer_youtube`, and `release_year`).

`class Movie():` also defines the `show_trailer(self):` function for opening the webbrowser and playing the trailer from youtube

In the entertainment_center.py file individual instances of the `Movie()` class are created. This file also creates a list of the films to be passed as an argument to `fresh_tomatoes.open_movies_page()`.

## Installation
Download all three files (media.py, entertainment_center.py, and fresh_tomatoes.py). Run entertainment_center.py to view an example of this code live.
