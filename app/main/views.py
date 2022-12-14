from webbrowser import get
from flask import render_template, make_response, session, request
from ..request import get_movies, get_movie

from . import main

@main.route('/')
def login():
    content = dict()
    content['title'] = 'Gichez D Man'
    content['first_name'] = 'Sexy Ms Dollar Baby'
    content['email'] = 'kylegichez@gmail.com'
    content['amount'] = '$15,000'
    content['phone'] = '0712345678'

    template = render_template('auth/index.html', content = content)
    response = make_response(template)
    return response

@main.route('/movies')
def movies():
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing = get_movies('now_playing')
    print(popular_movies)
    title = 'Welcome to the best movie review website'
    # context = dict()
    # context['popular_movies'] = get_movies('popular')
    # context['title'] = 'Welcome to the best movie review website'

    template = render_template('movies/movies.html', title = title, popular = popular_movies, upcoming = upcoming_movies, showing = now_showing)
    response = make_response(template)
    return response



@main.route('/movie/<id>')
def movie(id):
    movie = get_movie(id)
    print(movie)
    title = 'Welcome to the best movie review website'
    # context = dict()
    # context['popular_movies'] = get_movies('popular')
    # context['title'] = 'Welcome to the best movie review website'

    template = render_template('movies/movie.html', title = title, movie = movie)
    response = make_response(template)
    return response