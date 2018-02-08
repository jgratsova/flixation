from __future__ import print_function
import sys
import os
import logging
from flask import Flask, redirect, url_for, request, render_template
from common.database import Database
from models.movie import Movie
from models.user import User
from flask import session, make_response


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/login') # www.mysite.com/api
def login_template():
    return render_template('login.html')


@app.route('/register')
def register_template():
    return render_template('register.html')

@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        print("test")
        User.login(email)
    else:
        session['email'] = None

    movies = Movie.from_all()
    return render_template('movies.html', movies=movies, email = session['email'])


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email, password)
    movies = Movie.from_all()

    return render_template('movies.html', movies=movies, email = session['email'])



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/movies')
def user_movies():

    movies = Movie.from_all()
    print('DEBUG MESSAGE', file=sys.stderr)
    print(movies, file=sys.stderr)
    return render_template('movies.html', movies=movies, email = session['email'])

@app.route('/movies/<string:movie_file>')
def movie(movie_file):
    single_movie = Movie.from_mongo(movie_file)

    return render_template('movie.html', single_movie=single_movie)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
