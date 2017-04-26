from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

setup(
    name='moviedatamaker',

    version='0.0.1',

    description='A script that looks up all movies and TV shows in a folder and gets the  genre, runtime, plot and IMDB and RottenTomatoes ratings of the movie and stores it as a csv file.',

    url='https://github.com/anubhabsen/movie-info',

    author='Anubhab Sen',
    author_email='anubhabsen@gmail.com',

    license='BSD 2',

    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],

    keywords='movie data info information scrap imdb rottentomatoes',

    py_modules=["moviedatamaker"],

    install_requires=['pandas', 'lxml', 'requests', 'guessit'],
)